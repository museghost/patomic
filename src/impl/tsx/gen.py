from __future__ import print_function


def _get_prologue(name):
    name = "_".join(name.upper().split())
    template = "#ifndef PATOMIC_IMPL_TSX_PP_%s_H\n"
    template += "#define PATOMIC_IMPL_TSX_PP_%s_H\n\n"
    return template % (name, name)


def _get_epilogue(name):
    name = "_".join(name.upper().split())
    template = "\n#endif  /* !PATOMIC_IMPL_TSX_PP_%s_H */\n"
    return template % (name,)


def _get_warning():
    return "/* NOTE: this file is auto-generated by gen.py */\n\n"


def create_repeat(n):
    name = "repeat"

    content = _get_prologue(name)
    content += _get_warning()
    content += "#define PATOMIC_TSX_REPEAT_N %s\n\n" % n
    content += "#define PATOMIC_TSX_REPEAT(def) \\\n"
    for i in range(n - 1):
        content += "    def(%s) \\\n" % (i + 1,)
    content += "\n"
    content += _get_epilogue(name)

    with open(name + ".h", "w") as f:
        f.truncate()
        f.write(content)

    out = "Created %s.h with n=%s" % (name, n)
    print(out)


if __name__ == "__main__":
    repeats = 0x4000
    create_repeat(repeats)
