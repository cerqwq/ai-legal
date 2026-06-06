# ⚖️ AI Legal

AI法律工具，支持合同审查、法律咨询、文书生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📄 合同审查
- 📝 合同生成
- 💬 法律咨询
- 📋 法律文书生成
- ⚠️ 法律风险分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_legal import create_tools

tools = create_tools()

# 合同审查
review = tools.review_contract(contract_text)

# 合同生成
contract = tools.generate_contract("服务合同", parties, terms)

# 法律咨询
consultation = tools.legal_consultation("劳动纠纷问题", "中国")

# 法律文书
document = tools.generate_legal_document("起诉状", details)

# 风险分析
risk = tools.analyze_legal_risk(situation)
```

## 📁 项目结构

```
ai-legal/
├── tools.py       # 法律工具核心
└── README.md
```

## 📄 许可证

MIT License
