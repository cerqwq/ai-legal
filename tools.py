"""
AI Legal - AI法律工具
支持合同审查、法律咨询、文书生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AILegalTools:
    """
    AI法律工具
    支持：合同、咨询、文书
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def review_contract(self, contract_text: str) -> Dict:
        """审查合同"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请审查以下合同：

{contract_text[:2000]}

请返回JSON格式：
{{
    "risk_level": "high/medium/low",
    "issues": [
        {{"clause": "条款", "risk": "风险", "suggestion": "建议"}}
    ],
    "missing_clauses": ["缺失条款"],
    "overall_assessment": "总体评价"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"review": content}

    def generate_contract(self, contract_type: str, parties: Dict, terms: Dict) -> str:
        """生成合同"""
        if not self.client:
            return "LLM客户端未配置"

        parties_text = json.dumps(parties, ensure_ascii=False)
        terms_text = json.dumps(terms, ensure_ascii=False)

        prompt = f"""请生成{contract_type}合同：

当事方：{parties_text}
条款：{terms_text}

要求：
1. 标准格式
2. 条款完整
3. 权责清晰"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def legal_consultation(self, question: str, jurisdiction: str) -> Dict:
        """法律咨询"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请回答以下法律问题：

问题：{question}
司法管辖区：{jurisdiction}

请返回JSON格式：
{{
    "answer": "回答",
    "relevant_laws": ["相关法律"],
    "precedents": ["先例"],
    "recommendations": ["建议"],
    "disclaimer": "免责声明"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"consultation": content}

    def generate_legal_document(self, document_type: str, details: Dict) -> str:
        """生成法律文书"""
        if not self.client:
            return "LLM客户端未配置"

        details_text = json.dumps(details, ensure_ascii=False)

        prompt = f"""请生成{document_type}：

详细信息：{details_text}

要求：
1. 标准格式
2. 用语规范
3. 条款完整"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_legal_risk(self, situation: str) -> Dict:
        """分析法律风险"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下情况的法律风险：

{situation}

请返回JSON格式：
{{
    "risk_level": "high/medium/low",
    "risks": [
        {{"risk": "风险", "probability": "概率", "impact": "影响", "mitigation": "缓解措施"}}
    ],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"risk_analysis": content}


def create_tools(**kwargs) -> AILegalTools:
    """创建法律工具"""
    return AILegalTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Legal Tools")
    print()

    # 测试
    review = tools.review_contract("甲方：XXX公司\n乙方：YYY公司\n...")
    print(json.dumps(review, ensure_ascii=False, indent=2))
