import pandas as pd


class SGroup(object):
    def __init__(self, filename):
        self.data = self.read(filename)

    def read(self, filename):
        data_list = []
        line_num = 0
        with open(filename) as f:
            for line in f:
                line_num += 1
                if line_num == 1: continue
                infos = line.strip().split('|')
                code = infos[0]
                start_date = int(infos[1])
                end_date = int(infos[2]) if infos[2] != 'None' else 99999999
                cateory = infos[3]
                info = {'code': code, 'start_date': start_date, 'end_date': end_date, 'cateory': cateory}
                data_list.append(info)
        return pd.DataFrame(data_list)

    def get_cateory(self, code, query_date):
        infos = self.data.loc[self.data.code == code]
        info = infos.loc[(infos.start_date <= query_date) & (infos.end_date >= query_date)]
        if info.empty: return None
        if len(info) > 1:
            raise Exception("multiple category for {} in {}".format(code, query_date))
        return info['category'].iloc[0]


if __name__ == '__main__':
    filename = 'sample.txt'
    sg = SGroup(filename)
    sg.get_cateory('100', 20101109)
