adjs = []
nouns = []
options = []
output_styles = []
styles = []
detail_levels = []

component = {'adjs': adjs,
             'nouns': nouns,
             'options': options,
             'output_styles': output_styles,
             'styles': styles,
             'detail_levels': detail_levels}

for key, val in component.items():
    with open(f'{key}.txt', 'r') as f:
        lst = list(map(lambda x: x.strip(), f.readlines()))
        val.extend(lst)


def main():
    num_gen = int(
        input("Enter the number of generation queries for Chat - GPT: "))
    count = 0
    with open('../prompts.txt', 'w') as f:
        for adj in adjs:
            for noun in nouns:
                for option in options:
                    for output_style in output_styles:
                        count += 1
                        lst = [adj, option,
                               output_style, noun]
                        txt = " ".join(lst)
                        f.write(
                            f'Generate a script for Midjourney to draw a {txt} in form of keywords, separate with commas \n')
                        if (count == num_gen):
                            return


if __name__ == '__main__':
    main()
