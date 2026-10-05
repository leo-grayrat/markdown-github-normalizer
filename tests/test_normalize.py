import unittest

from mdgithub_normalizer.normalize import normalize_markdown


class NormalizeMarkdownTests(unittest.TestCase):
    def test_converts_bracket_display_math_to_fenced_math_with_blank_lines(self):
        source = "前文\n\\[\nx_i = 1\n\\]\n后文\n"
        expected = "前文\n\n```math\nx_i = 1\n```\n\n后文\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_converts_dollar_display_math_and_preserves_blank_lines_and_markdown_like_lines(self):
        source = "前文\n$$\na=1\n\n+ b\n=\nc\n$$\n后文\n"
        expected = "前文\n\n```math\na=1\n\n+ b\n=\nc\n```\n\n后文\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_converts_indented_display_math_without_breaking_list_container(self):
        source = "1. 条目\n   $$\n   x=1\n\n   + y\n   $$\n   继续说明\n"
        expected = "1. 条目\n   ```math\n   x=1\n\n   + y\n   ```\n   继续说明\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_converts_blockquoted_display_math_and_preserves_quote_prefix(self):
        source = "> 前文\n> \\[\n> x=1\n> \\]\n> 后文\n"
        expected = "> 前文\n> ```math\n> x=1\n> ```\n> 后文\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_unclosed_display_math_is_left_unchanged(self):
        source = "前文\n$$\nx=1\n"
        expected = "前文\n\n$$\nx=1\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_protects_inline_math_and_preserves_spacing_commands(self):
        source = "中文$x\\;y\\,z$中文，另有\\(q+1\\)正文。\n"
        expected = "中文 $`x\\;y\\,z`$ 中文，另有 $`q+1`$ 正文。\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_preserves_spacing_commands_inside_existing_protected_math(self):
        source = "前文 $`a\\,b\\;c`$ 后文\n"
        self.assertEqual(normalize_markdown(source), source)

    def test_repairs_known_tex_compatibility_forms_without_rewriting_spacing(self):
        source = "$$\n\\operatorname{vec}(D\\_{m}) \\cross x \\; y \\, z\n$$\n"
        expected = "```math\n\\mathrm{vec}(D_{m}) \\times x \\; y \\, z\n```\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_replaces_makebox_with_mbox_and_drops_layout_arguments(self):
        source = (
            "```math\n"
            "\\makebox{hello}\n"
            "\\makebox[4em]{hello}\n"
            "\\makebox[4em][r]{hello}\n"
            "\\makebox[0pt][r]{第1行}\n"
            "\\makebox[4em][c]{\\frac{x}{y}}\n"
            "\\boxed{x+y} \\fbox{hello} \\mbox{hello} \\text{hello}\n"
            "```\n"
        )
        expected = (
            "```math\n"
            "\\mbox{hello}\n"
            "\\mbox{hello}\n"
            "\\mbox{hello}\n"
            "\\mbox{第1行}\n"
            "\\mbox{\\frac{x}{y}}\n"
            "\\boxed{x+y} \\fbox{hello} \\mbox{hello} \\text{hello}\n"
            "```\n"
        )
        self.assertEqual(normalize_markdown(source), expected)

    def test_existing_math_fence_uses_same_repairs(self):
        source = "```math\n\\operatorname{rank}(A) \\cross B \\; C\n```\n"
        expected = "```math\n\\mathrm{rank}(A) \\times B \\; C\n```\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_repairs_bold_internal_space_and_punctuation_boundaries(self):
        source = "前文**结论：**正文\n**123 **后文\n"
        expected = "前文**结论：** 正文\n\n**123** 后文\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_plain_bold_stays_attached_to_surrounding_text(self):
        source = "中文**控制命令**中文\n"
        self.assertEqual(normalize_markdown(source), source)

    def test_punctuation_outside_bold_does_not_trigger_spacing(self):
        source = "发下去的**控制命令**，和反馈回来的**机器人状态**。\n"
        self.assertEqual(normalize_markdown(source), source)

    def test_opening_punctuation_inside_bold_adds_space_before_opener(self):
        source = "中文**，控制命令**中文\n中文**（控制命令**中文\n中文**“控制命令**中文\n"
        expected = "中文 **，控制命令**中文\n\n中文 **（控制命令**中文\n\n中文 **“控制命令**中文\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_closing_punctuation_inside_bold_adds_space_after_closer(self):
        source = "中文**控制命令，**中文\n中文**控制命令）**中文\n一个**工作空间（workspace）**里管理\n"
        expected = "中文**控制命令，** 中文\n\n中文**控制命令）** 中文\n\n一个**工作空间（workspace）** 里管理\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_multiple_bold_spans_do_not_pair_across_boundaries(self):
        source = "父子中位延迟比仅约 **1.002 倍**。两项可运行的动作及普通对照均记为**未判定**，而非无效。\n"
        self.assertEqual(normalize_markdown(source), source)

    def test_does_not_add_spaces_between_bold_and_punctuation(self):
        source = "（**结论**），下一句。\n"
        self.assertEqual(normalize_markdown(source), source)

    def test_code_regions_are_untouched(self):
        source = (
            "`\\(x\\) \\operatorname{vec} D\\_{m} \\cross y \\,z\\;w **123 **`\n"
            "```text\n"
            "\\(x\\) \\operatorname{vec} D\\_{m} \\cross y \\,z\\;w **123 **\n"
            "```\n"
        )
        self.assertEqual(normalize_markdown(source), source)

    def test_escaped_bold_markers_are_untouched(self):
        source = "\\*\\*不是加粗\\*\\*\n"
        self.assertEqual(normalize_markdown(source), source)

    def test_typora_single_newline_becomes_paragraph_break(self):
        source = "第一句话\n第二句话\n\n第三句话\n"
        expected = "第一句话\n\n第二句话\n\n第三句话\n"
        self.assertEqual(normalize_markdown(source), expected)

    def test_does_not_split_structured_markdown(self):
        source = (
            "- 第一项\n"
            "- 第二项\n\n"
            "| A | B |\n"
            "| - | - |\n"
            "| 1 | 2 |\n\n"
            "> 引用第一行\n"
            "> 引用第二行\n\n"
            "```text\n"
            "$x$ **123 ** \\(literal\\)\n"
            "```\n"
        )
        self.assertEqual(normalize_markdown(source), source)

    def test_is_idempotent(self):
        source = (
            "前文\\(x\\,y\\)正文\n"
            "$$\n"
            "\\operatorname{vec}(D\\_{m}) \\cross z \\; q\n\n"
            "+ c\n"
            "$$\n"
            "后文\n"
        )
        once = normalize_markdown(source)
        self.assertEqual(normalize_markdown(once), once)


if __name__ == "__main__":
    unittest.main()
