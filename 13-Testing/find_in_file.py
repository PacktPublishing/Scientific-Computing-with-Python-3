class NotFoundError(Exception):
  pass

def find_string(file, string):
    for i,lines in enumerate(file.readlines()):
        if string in lines:
            return i
    raise NotFoundError(
         'String {} not found in File {}'.format(string,file.name))
