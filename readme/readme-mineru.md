
uv venv
source .venv/bin/activate
# export HF_ENDPOINT=https://hf-mirror.com


uv pip install -e '.[core]' -i https://mirrors.aliyun.com/pypi/simple

# 模型测试
mineru -p /Users/yangcailu/chengtay_code/markdown/hutool1083865541173075661.pdf -o /Users/yangcailu/chengtay_code/markdown/output
export MINERU_MODEL_SOURCE=modelscope
mineru-api --host 0.0.0.0 --port 8100

# mcp 相关
cd  projects/mcp      
uv venv
source .venv/bin/activate
uv run mineru-mcp --transport streamable-http --port 8101 --host 0.0.0.0