class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)


    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"



    def find(self, value):
        result = []
        for i in range(len(self.scores)):
            if self.scores[i] == value:
                result.append(i)
        return result


    def get_sorted(self):
        scores = self.scores.copy()
        number = len(scores)

        for i in range(number):
            for j in range(0, number - i - 1):
                if scores[j] > scores[j + 1]:
                    temp = scores[j]
                    scores[j] = scores[j + 1]
                    scores[j + 1] = temp
        return scores

#bonus1
    def average(self):
        return sum(self.scores) / len(self.scores)

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)


    def pass_rate(self):
        passed = 0
        for i in self.scores:
            if i >= 50:
                passed += 1

        return passed / len(self.scores)

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"

#bonus2

    #def find(self):

    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None  # zatím nic neseřazené

    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting...")
            self._sorted_scores = self.get_sorted()
        hodnoty = self._sorted_scores

        left = 0
        right = len(hodnoty) - 1

        while left < right:
            mid = (left + right) // 2

            if hodnoty[mid] == hodnoty[left]:
                return mid
            elif hodnoty[mid] < score:
                left = mid + 1

            else:
                right = mid - 1
        return None



    #
    # scores = [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # score = 91
    # left = 0
    # print("sorting...")
    # hodnoty = sorted(scores)
    # print("Zoradené:", hodnoty)
    # right = len(hodnoty) - 1
    #
    # left = 0
    # right = len(hodnoty) - 1
    #
    # while left < right:
    #     mid = (left + right) // 2
    #
    #     if hodnoty[mid] == hodnoty[left]:
    #         result = mid
    #         break
    #     elif hodnoty[mid] < score:
    #         left = mid + 1
    #
    #     else:
    #         right = mid - 1
    # print("Výsledok indexu:", result)