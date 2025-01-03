from saxonche import PySaxonProcessor
import os
import logging

logging.basicConfig(level=logging.INFO)
script_dir = os.path.dirname(os.path.abspath(__file__))
source_file = os.path.join(script_dir, "input", "books.xml")
xsl_file = os.path.join(script_dir, "xsl", "books.xsl")
output_file = os.path.join(script_dir, "output", "books.html")

with PySaxonProcessor(license=False) as proc:
    transformer = proc.new_xslt30_processor()
    try:
        transformer.transform_to_file(source_file=source_file, stylesheet_file=xsl_file, output_file=output_file)
        logging.info(f"Transformation successful. Output file: {output_file}")
    except Exception as e:
        logging.error(f"Transformation failed: {e}")

