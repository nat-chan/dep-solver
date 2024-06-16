from packaging.requirements import Requirement

# バージョン指定の例
requirement_strings = ["diffusers<0.29.0", "diffusers>=0.25.0"]

# 各要求に対して正規化を行う
for req_string in requirement_strings:
    requirement = Requirement(req_string)
    normalized_name = requirement.name
    specifier_set = requirement.specifier
    print(f"正規化されたパッケージ名: {normalized_name}")
    print(f"正規化されたバージョン指定: {specifier_set}")
