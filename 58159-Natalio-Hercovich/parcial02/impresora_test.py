import unittest
from impresora import Printer

class TestPrinter(unittest.TestCase):

    def test_printer_avialable(self):
        impresora = Printer()
        printer_ok = impresora.printer_available
        self.assertTrue(printer_ok)

    def test_print_job(self):
        impresora = Printer()
        printer_ok = impresora.print_job
        self.assertTrue(printer_ok)

    def test_print_job2(self):
        impresora = Printer()
        impresora.print_job()
        self.assertTrue(impresora.error_flag)

    def test_reset_printer(self):
        impresora = Printer()
        impresora.reset_printer()
        self.assertFalse(impresora.printing)



    

















if __name__ == '__main__':
   unittest.main()