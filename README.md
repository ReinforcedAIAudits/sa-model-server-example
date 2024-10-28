# Solidity Audit Model Server Example

Here is an example of a model server implementation based on [Microsoft's Phi-3.5](https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF) model, running on CPU with [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) (it should work on any modern server CPU and provide acceptable response times).

This implementation is recommended for use in testing, for running the miner in our testnet, and as a template for creating your own server with a more powerful model. The model used in this implementation does not serve the purpose well. `llama-cpp-python` can utilize GPU by specifying the argument `n_gpu_layers=-1` when initializing the model, for example:

```python
llm = Llama(
    model_path="Phi-3.5-mini-instruct-Q6_K_L.gguf", n_ctx=int(os.getenv('CONTEXT_SIZE', '8192')), n_gpu_layers=-1
)
```

The easiest way to run the model server is using Docker with the command `docker compose up -d`. You can query the model server using the `test_quality.py` file, which requires no additional dependencies and runs with built-in `python3` on Ubuntu or macOS.
