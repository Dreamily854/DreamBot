### DreamBot 配置文件详解

---

让我们来看一个例子: `config.json`

```json
{
    "http": {
        "server": "0.0.0.0",
        "port": 5580
    },
    "send": {
        "server": "0.0.0.0",
        "port": 5700,
        "token": ""
    },
    "command": [
        {
            "prefix": "/",
            "mode": "handle"
        },
        {
            "prefix": ".aa",
            "mode": "proxy",
            "csend": {
                "server": "0.0.0.0",
                "port": 5580
            },
            "access_token":""
        }

    ]
}
```

---

### `http` 接收go-cqhttp上报数据及其他请求部分
| 参数 | 描述 |
| :-: | :-: |
| server | HTTP服务器监听地址 |
| port | HTTP服务器监听端口 |
==注意:此部分在使用WSGI时无效==

### `send` 发送消息，机器人操作使用接口
| 参数 | 描述 |
| :-: | :-: |
| server | 发送地址 |
| port | 发送端口 |

### `command` 命令处理部分
DreamBot 支持处理多个前缀
| 参数 | 描述 |
| :-: | :-: |
| prefix | 前缀 |
| mode | 处理模式 |


###### `csend` 发送消息，消息发送到其它程序中处理。发送方式为POST
| 参数 | 描述 |
| :-: | :-: |
| server | 发送地址 |
| port | 发送端口 |

proxy 代表该含有该前缀的消息将被发送到其它程序处理，handle代表将使用自带命令处理器处理消息
