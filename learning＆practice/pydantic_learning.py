#-------------------#
### 1.pydantic for LLM

# pydantic是一个用于LLM工作流的结构化输出包。
# LLM一般输出自由文本。当需要把LLM作为组件集成进入一个更大的整体，结构化输出就非常有用

#-------------------#
### 2.pydantic for LLM工作流
## 方法一：直接在prompt要求LLM返回结构化结果：JavaScript Object Notation（JSON）
#   直接这么做，LLM有可能生成JSON格式以外的信息，所以需要使用pydantic
# 使用pydantic可以定义数据类型，明确开发者期望的数据结构和返回值类型
# pydantic BaseModel类的model_validate_json(llm_output)函数来检验LLM的输出是否符合开发者确立的JSON格式，如果不符合则返回给LLM让它进行修改

from pydantic import basemodel


## 方法二：在初始请求时直接传入pydantic数据模型（在API调用中明确表达了需求，可以更可靠地获得需要的结果）

#-------------------#
### 3.pydantic模型基础