# 项目结构

> 目录结构：
- data 
    - raw 原始JD
    - processed 处理后的结构化输入
- src 代码
- tests 测试


## 手搓demo时间线
- D1：
    - 在招聘网站复制5份agent相关岗位描述，不同JD之间有一些差异。
    - 人工决定：从raw_data中应该抽取什么信息（对于agent岗的招聘而言，什么信息值得结构化？）第一天就要固定schema，因为后续统计/筛选/SQL/召回/排序均依赖结构化字段。
        - 公司
            - 大厂
            - 中厂
            - 初创
        - 岗位分类
            - agent开发
            - agent评测
            - agent算法
        - 到岗时间
            - 4天
            - 5天
        - 实习时长
            - 3-6个月
            - 6个月以上
        - 编程语言
            - python
            - JAVA
            - python/GO/Scala任一
        - agent技能
            - MCP
            - skills
            - langgraph/langchain
            - ReAct
            - RAG
        - 工程技能
            - 后端经验
            - 408基础
        - 论文发表要求
            - 必须
            - 加分项
        - 工作内容概述