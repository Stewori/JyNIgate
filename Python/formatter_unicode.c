/* Implements the unicode (as opposed to string) version of the
   built-in formatter for unicode.  That is, unicode.__format__(). */

#include "Python_JyNI.h"

#ifdef Py_USING_UNICODE

#include "stringlib/unicodedefs.h"

#define FORMAT_STRING _PyUnicode_FormatAdvanced

/* don't define FORMAT_LONG, FORMAT_FLOAT, and FORMAT_COMPLEX, since
   we can live with only the string versions of those.  The builtin
   format() will convert them to unicode. */

#include "stringlib/formatter.h"

#endif
