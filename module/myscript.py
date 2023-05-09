# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリ
import sys
sys.path.append("/Users/mariacron/Desktop/PythonLecture/function")
import docstring
# import mymodule as mm
# from mymodule import myfunc,myvariable,anotherfunc
# 何がインポートされているかわからないため、非推奨
# from mymodule import *


print(sys.path)
# mm.myfunc()
#
# mm.anotherfunc()
#
# print(mm.myvariable)

print(docstring.multiply(3, 5))
