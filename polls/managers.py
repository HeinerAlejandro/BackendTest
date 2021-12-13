import operator

from django.db.models import Manager, Avg

from .choices import AgeTypes


class PollManager(Manager):
    def age_most_uses_sn(self, sn: str) -> str:
        """ Return range age that most uses the social network given """

        query = self.get_queryset()

        if query.count() == 0:
            return AgeTypes.FROM_18_25.value

        data = {}

        for age in AgeTypes.values:
            avg = query\
                .filter(age=age)\
                .aggregate(
                    social=Avg(f'time_{sn}_avg')
                )
            if avg['social']:
                data[age] = avg['social']

        age_range = max(data.items(), key=operator.itemgetter(1))[0]

        return age_range
