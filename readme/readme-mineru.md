
# 机器：10.40.0.124 GPU 5880 48G
cd /home/ubuntu/chengtay_code/MinerU/

source .venv/bin/activate
<!-- uv venv -->
uv venv
# export HF_ENDPOINT=https://hf-mirror.com


uv pip install -e '.[core]' -i https://mirrors.aliyun.com/pypi/simple

# 模型测试
mineru -p /home/luyangcai/code/MinerU/demo/pdfs/demo1.pdf -o /home/luyangcai/code/MinerU/demo/output
# 第一次下载的时候，需要下载model，故需通过 modelscope启动
export MINERU_MODEL_SOURCE=modelscope
# 后续启动可以通过 local 启动
export MINERU_MODEL_SOURCE=local
# 如未设置 MINERU_MODEL_SOURCE，默认使用 huggingface 模型,会造成模型访问失败。

静默启动 MinerU API（后台运行、无控制台输出）：
nohup uvicorn mineru.cli.fast_api:app --host 0.0.0.0 --port 8100 --workers 4 --log-level critical >> mineru-api.log 2>&1 &

# mcp 相关
cd  projects/mcp      
uv venv
source .venv/bin/activate
静默启动 MCP 服务（后台运行、无控制台输出）：
nohup uv run mineru-mcp --transport streamable-http --port 8101 --host 0.0.0.0 >> mcp.log 2>&1 &