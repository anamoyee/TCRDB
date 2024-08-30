import tcrutils as tcr

import tcrdb


def test_default_dict_db():
  class StrDB(tcrdb.DefaultDictDB[str], dir='./test1'):
    def default_factory(self, key: str) -> str:
      return 'default_value'


  StrDB = StrDB()

  StrDB.get()

  tcr.c(StrDB)
  StrDB[1]
  tcr.c(StrDB)
  tcr.c(StrDB[1])
  StrDB[2] = 'nya'
  tcr.c(StrDB)

if True:  # \/ # Test setup
  for k, v in globals().copy().items():  # Decorate each test_... function with the @tcr.test decorator
    if k.startswith('test_'):
      globals()[k] = tcr.test(v)

if __name__ == '__main__':
  test_default_dict_db()
