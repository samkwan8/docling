from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # PDF path or URL
converter = DocumentConverter()
doc = converter.convert(source=source)
print(doc.render_as_markdown_v1())  # output: ## Docling Technical Report [...]"
