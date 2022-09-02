# WARP+

设置步骤：

1. `Fork`当前仓库
2. 移动端下载[1.1.1.1](https://cloudflarewarp.com/)，并获取设备ID（设置 > 高级 > 诊断）

   <img src="https://user-images.githubusercontent.com/70625361/187929196-ab20a5df-dd4b-4752-ae4e-6771738d768a.jpg" width="200px" >


3. 设置仓库私密环境变量（New repository secret）

   ![QQ截图20220901213213](https://user-images.githubusercontent.com/70625361/187928983-17d614e2-c505-4282-893b-e05823530dfb.png)

运行方式：

- 定时任务：每天12:00运行，每次运行1小时（需修改`.github/workflows/main.yml`文件，手动启用）

- 手动运行

  ![image](https://user-images.githubusercontent.com/70625361/187930606-2cfb2bd9-01b4-4b53-a4bf-1617fd0ea9a6.png)

> 每次执行将启用10个job并发运行（大约每2.3秒获取1GB流量）
> 
> GitHub Action免费计划每月只能运行2000分钟

****

[参考源](https://github.com/ALIILAPRO/warp-plus-cloudflare)
