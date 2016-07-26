from pdf_extractor.run_ocr import OCR
import io


def main():
	p = OCR("tests/ImageOnly.pdf", "INFO", "none")
	p.start()

	against = ""

	with io.open('tests/PlainText.txt') as f:
		against = f.read()

	assert(p.text == against)


if __name__ == '__main__':
	main()
