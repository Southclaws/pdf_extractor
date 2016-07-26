#!/usr/bin/env python3
import argparse
import logging
import subprocess


class OCR():
	def __init__(self, filename, loglevel="NONE", outmode="none"):
		self.initialised = False

		if loglevel != "NONE":
			logging.basicConfig(filename="pdf_extractor.log", level=getattr(logging, loglevel.upper()))

		self.filename = filename
		self.loglevel = loglevel
		self.outmode = outmode

		self.text = ""

		self.initialised = True

	def start(self):
		if not self.initialised:
			logging.error("ERROR: OCR not initialised, cannot run")
			return

		try:
			self.text = subprocess.check_output([
				'doc_worker',
				'-m',
				'-l', self.loglevel,
				self.filename,
				'stdout'

			]).decode('utf-8')

		except PermissionError as e:
			print(e)
			print("You may need to chmod +x 'doc_worker'")

		if self.outmode == "stdout":
			print(self.text)

		elif self.outmode == "count":
			print("Extracted", len(self.text), "text")


def main():
	parser = argparse.ArgumentParser(description='Run OCR on PDF files.')
	parser.add_argument('pdf', type=str, help='PDF files to process')
	parser.add_argument('out', type=str, help='stdout|count|none')
	parser.add_argument("-l", "--loglevel", default="WARNING", help="set logging level")
	args = parser.parse_args()

	p = OCR(args.pdf, args.loglevel, args.out)
	p.start()


if __name__ == '__main__':
	main()
