# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.4
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any

class PageHeader:

    def __init__(self, page_content: PageContent) -> None:
        self.page_content = page_content

    def get_home_header(
            self, *args: Any, **kwargs: Any) -> gr.Markdown:
        our_heading = gr.Markdown(
            self.page_content.home_header
        )

        return our_heading

    def get_preprocessing_header(
            self, *args: Any, **kwargs: Any) -> gr.Markdown:
        our_preprocessing_header = gr.Markdown(
            self.page_content.preprocessing_header
        )

        return our_preprocessing_header
