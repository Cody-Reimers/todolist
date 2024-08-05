
import data_validation as dv

###############################################################################



###############################################################################

class Todo:

    DONE_OR_NOT_STRING = {True: "X", False: " "}

    #~~~~INITIALIZATION~~~~#

    def __init__(self, name, done_or_not=False):
        self._name = name
        self.is_done = done_or_not

    #~~~~REPRESENTATIONS~~~~#

    def __str__(self):
        done_or_not = self.__class__.DONE_OR_NOT_STRING[self.is_done]

        return (f"[{done_or_not}] {self.name}")

    #~~~~RICH COMPARISONS~~~~#

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return (self.name == other.name) and (self.is_done == other.is_done)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return (self.name != other.name) or (self.is_done != other.is_done)

    #~~~~GETTER METHODS~~~~#

    @property
    def name(self):
        return self._name

    @property
    def is_done(self):
        return self._is_done

    #~~~~SETTER METHODS~~~~#

    @is_done.setter
    def is_done(self, done_or_not):
        ref = "Todo List Element Done Flag"

        dv.error_not_bool(done_or_not, ref)

        self._is_done = done_or_not

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#//////////////////////////////////////////////////////////////////////////////

###############################################################################


