INFOS = """
## 关于 MAA | About MAA
- **[官网](https://maa.plus)**
- **[Github 仓库](https://github.com/MaaAssistantArknights/MaaAssistantArknights)**
- **[用户 QQ 群](https://ota.maa.plus/MaaAssistantArknights/api/qqgroup)**

## 关于我们 | About Maa-Mirror
- **[关于我们](https://www.mmirror.top/about.html)**

## 注意事项 | Note
> [!IMPORTANT]
> - Maa-Mirror 仅提供国内网盘分流，不受理 Maa 使用相关问题，请移步 **[MAA 用户 QQ 群](https://ota.maa.plus/MaaAssistantArknights/api/qqgroup)** 。
> - Maa-Mirror 可能会不定期删除历史版本以释放可用空间。如有下载特定历史版本的需求，推荐前往 **[Github Release](https://github.com/MaaAssistantArknights/MaaAssistantArknights/releases)** 下载。

## 问题反馈 | Feedback
如确认无相关 **[公告]({NOTICE_URL})** ，请通过下列方式联系我们：
- 前往 **[Maa-Mirror-Issue](https://github.com/MaaMirror/Maa-Mirror-Issue/issues)** 创建 issue 。
- 发送邮件至 **<a href="mailto:weinibuliu@outlook.com">weinibuliu@outlook.com</a>**
> [!WARNING]
> 请勿反馈 **历史版本** 缺失问题。
"""

BODY = (
    """## 更新日志 | Release Note
<details>

<summary>点击查看</summary>

{NOTE}

</details>

## 下载地址 | Download
> MAA 更新时间 | 镜像更新时间
> --- | ---
> {RELEASE_TIME} | {TIME}

- **[Maa-Mirror]({DOWNLOAD_URL})**
- [Github](https://github.com/MaaAssistantArknights/MaaAssistantArknights/releases/{VERSION})
"""
    + INFOS
)


RESOURCE = (
    """## 资源信息 | Resource Info
- 资源版本: {RES_VER}
- 资源日期: {RES_TIME}

## 下载地址 | Download
>[!IMPORTANT]
> 资源分流将保持最新，Maa-Mirror 不会提供其历史版本。

> 镜像更新时间: {TIME}

- **[Maa-Mirror]({DOWNLOAD_URL})**

## 使用方式 | How to Use
- 解压 `Resource.zip(.7z)` 得到 `cache` 与 `resource` 两个文件夹。
- 将上述文件夹**覆盖**MAA 安装目录下的**同名文件夹**。
- 重启 MAA 。

> - **视频教程: https://www.bilibili.com/video/BV13w4m1k7j3**
> - Github: https://github.com/MaaAssistantArknights/MaaAssistantArknights/issues/10033
"""
    + INFOS
)
