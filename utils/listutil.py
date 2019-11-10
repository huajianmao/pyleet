
class ListUtil:
  @classmethod
  def sortListOfLists(cls, lst):
    lst.sort()
    for it in lst:
      it.sort()
