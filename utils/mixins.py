__all__ = (
    'ReprMixin',
)


class ReprMixin:
    def __repr__(self):
        return self.__str__()
