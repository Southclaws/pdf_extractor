from pdf_extractor.run_ocr import OCR
import io


def main():
	p = OCR("tests/PlainText.pdf", "INFO", "none")
	p.start()

	result = p.text.strip()

	with io.open('tests/PlainText.txt') as f:
		against = f.read().strip()

	assert(result == against)

	print("Test passed.")


if __name__ == '__main__':
	main()
