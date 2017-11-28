import pandas as pd

def get_df_from_file(filename):
    return pd.DataFrame.from_csv(filename)
    pass

def extract_ref(df,ref_text_filename):
    df_group = df.groupby('mr')
    ref_texts = open(ref_text_filename, 'w')
    for df_mr in df_group:
        first_ref_text = df_mr[1]['ref'][0]
        #ref_texts.append(df_mr[1]['ref'][0])
        print >> ref_texts, first_ref_text




if __name__ == '__main__':
    filename = "/Users/shubhi/Documents/Fall 2017/Ind Study/tgen/e2e-challenge/input/e2e_data_personage_dev.csv"
    df = get_df_from_file(filename)
    ref_text_filename = 'dev_personage_ref.txt'
    extract_ref(df, ref_text_filename)
