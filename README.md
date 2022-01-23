# File API

## ToDo

- [x] Service path resolve pattern: `/file/{localSystemFilePath}`
- [ ] Support query parameter: orderBy, orderByDirection, filterByName
- [x] GET file: Return file or not found
- [x] GET directory: List folder or not found
- [x] POST file: Upload file if file not exist
- [x] PATCH file: Update file if file exist
- [x] DELETE file: Delete file if file exist
- [ ] Unit test
- [x] Run by docker compose
- [ ] Async IO

## Set up

- `docker-compose up`

## Try CRUD

- import `fileAPI.postman_collection.json` into postman.
- Execute APIs one by one from top to bottom.
- **The POST and PATCH API need to update file in person.**

## Result

- Get file folder
![1](./img/1.png)

- Post test.txt
![2](./img/2.png)

- Post REAME.md
![3](./img/3.png)

- Get root/usr folder
![4](./img/4.png)

- Get test.txt
![5](./img/5.png)

- Patch test.txt
![6](./img/6.png)

- Get test.txt
![7](./img/7.png)

- Delete test.txt
![8](./img/8.png)

- Get test.txt
![9](./img/9.png)

- Get root/usr/aabb folder
![10](./img/10.png)

- Terminal
![11](./img/11.png)