from distutils.core import setup


setup(
	name="pdf_extractor",
	description="Extracts text from PDF files, utilises multiple cores.",
	packages=["pdf_extractor"],
	version="0.1.0",
	author="Barnaby Keene",
	author_email="barnaby@spotlightdata.co.uk",
	url="https://github.com/Southclaw/pdf_extractor",
	license="GPLv3",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
		"Intended Audience :: Developers",
	],
	scripts=["doc_worker", "page_worker"]
)
