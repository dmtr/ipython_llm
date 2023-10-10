import llm
import re
import os
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

@magics_class
class LLMHelper(Magics):
    def __init__(self, shell, **kwargs):
        super().__init__(shell, **kwargs)
        self.model = llm.get_model("gpt-3.5-turbo")
        self.model.key = os.environ["OPENAI_API_KEY"]
        self.conversation = self.model.conversation()
        self.code_pattern = re.compile(r"```python(.*?)```", re.DOTALL)

    @line_magic
    def llm_prompt(self, line):
        opts, args = self.parse_options(line, 't:c:m', mode='string')
        model_opts = {"system": "Answer like a Python expert"}

        if model := opts.get("m"):
            model_name = llm.get_model_aliases().get(model)
            if not model_name:
                raise ValueError(f"Model {model} not found")
            self.model.get_model(model_name)

        if temperature := opts.get("t"):
            model_opts["temperature"] = float(temperature)

        if opts.get("c"):
            self.conversation = self.model.conversation()

        response = self.conversation.prompt(args, **model_opts)
        print("Waiting for response...")
        json_ = response.json()
        content = json_["content"]
        code =  self.code_pattern.findall(content)
        if code:
            return self.shell.set_next_input(code[0])
        else:
            print(content)


    @cell_magic
    def llm_prompt_cell(self, line, cell):
        return line, cell
