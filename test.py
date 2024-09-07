import tcrutils as tcr
from pydantic import BaseModel

import tcrdb


class Profile(BaseModel):
  name: str = 'Mike Rotch'
  age: int = 69
  height: float = 6.9

def test_default_dict_db():
  class PfDB(tcrdb.DefaultDictDB[Profile], dir='./test1'):
    def default_factory(self, key: str) -> str:
      return Profile()

  PFDB = PfDB()

  tcr.c(PFDB)

  with PFDB.cm(1) as pf:
    tcr.c(pf)
    pf.name += '!'
    tcr.c(pf)


  tcr.c(PFDB)



if True:  # \/ # Test setup
  for k, v in globals().copy().items():  # Decorate each test_... function with the @tcr.test decorator
    if k.startswith('test_'):
      globals()[k] = tcr.test(v)

if __name__ == '__main__':
  test_default_dict_db()
