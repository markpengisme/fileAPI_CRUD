from os import listdir, path, remove, makedirs, environ
from os.path import isfile, isdir
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

FILE_LOCATION = environ.get("FILE_LOCATION", "./file/")


def handle_uploaded_file(f, reqpath):
    with open(reqpath, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def restfulAPI(request, localSystemFilePath=''):
    reqPath = FILE_LOCATION + localSystemFilePath
    filepath, filename = reqPath.rsplit('/', 1)
    filepath += '/'
    print(reqPath, filepath, filename)

    # Get File or Directory
    if request.method == 'GET':
        if path.exists(reqPath):
            if filename == '':
                result = []
                for file in listdir(reqPath):
                    if isfile(reqPath+file):
                        result.append(file)
                    else:
                        result.append(file+'/')

                return JsonResponse({'status': True,
                                     'isDirectory': True,
                                     'files': result})
            elif isdir(reqPath):
                return JsonResponse(status=400,
                                    data={'status': 'False',
                                          'message': "Path '{}' is a directory.".format(reqPath)
                                          })
            else:
                return FileResponse(open(reqPath, 'rb'))
        else:
            return JsonResponse(status=404,
                                data={'status': 'False',
                                      'message': "Path '{}' Not Found".format(reqPath)
                                      })

    # localSystemFilePath ends with '/', not a filename
    # so can't do POST, PATCH, DELETE
    if filename == '':
        return JsonResponse(status=400, data={'status': 'False',
                                              'message': 'No filename in path'})

    # Create file by path
    if request.method == 'POST':
        print(request.FILES)
        if path.exists(reqPath):
            return JsonResponse(status=400, data={'status': 'False',
                                                  'message': 'File already exists'})

        file = request.FILES.get('file')
        if file is None:
            return JsonResponse(status=400, data={'status': 'False',
                                                  'message': 'File not in form data'})

        try:
            makedirs(filepath)
        except:
            None

        if isdir(filepath):
            handle_uploaded_file(file, reqPath)
            return JsonResponse(status=201, data={'status': 'True',
                                                  'message': 'File uploaded successfully'})
        else:
            return JsonResponse(status=400, data={'status': 'False',
                                                  'message': 'There are other files in the path instead of directories'})

    # Update file by path
    if request.method == 'PATCH':
        if not path.exists(reqPath):
            return JsonResponse(status=404, data={'status': 'False',
                                                  'message': 'File does not exist'})

        PUT, FILES = request.parse_file_upload(request.META, request)
        request.FILES.update(FILES)
        request.PUT = PUT.dict()
        file = request.FILES.get('file')
        if file is None:
            return JsonResponse(status=400, data={'status': 'False',
                                                  'message': 'File not in form data'})

        if isdir(filepath):
            handle_uploaded_file(file, reqPath)
            return JsonResponse(status=200, data={'status': 'True',
                                                  'message': 'File updated successfully'})
        else:
            return JsonResponse(status=400, data={'status': 'False',
                                                  'message': 'There are other files in the path instead of directories'})

    # Delete file by path
    if request.method == 'DELETE':
        if path.exists(reqPath) and isfile(reqPath):
            remove(reqPath)
            return JsonResponse(status=204,
                                data={'status': 'True',
                                      'message': "Delete file '{}' successfully".format(reqPath)
                                      })
        else:
            return JsonResponse(status=404,
                                data={'status': 'False',
                                      'message': "File '{}' Not Found".format(reqPath)
                                      })
