import argparse
import numpy as np
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="Convert a CHIRP formatted CSV to VGC formatted CSV import(s).")
    parser.add_argument('-i', '--input', help='filename, including path, of the CHIRP CSV file to convert.', 
                        required=True)
    parser.add_argument('-o', '--output', help='filename, including path, of the converted VGC formatted CSV.', required=True)
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()

def chirp_to_df(chirp_config):
    '''
    text
    '''
    df = pd.read_csv(chirp_config)
    return df

def create_vgc_df():
    '''
    '''
    df = pd.DataFrame(columns=['title',
                               'tx_freq',
                               'rx_freq',
                               'tx_sub_audio(CTCSS=freq/DCS=number)',
                               'rx_sub_audio(CTCSS=freq/DCS=number)',
                               'tx_power(H/M/L)',
                               'bandwidth(12500/25000)',
                               'scan(0=OFF/1=ON)',
                               'talk around(0=OFF/1=ON)',
                               'pre_de_emph_bypass(0=OFF/1=ON)',
                               'sign(0=OFF/1=ON)',
                               'tx_dis(0=OFF/1=ON)',
                               'mute(0=OFF/1=ON)',
                               'rx_modulation(0=FM/1=AM)',
                               'tx_modulation(0=FM/1=AM)'])
    return df

def divide_dataframes(input):
    '''
    '''
    pass

def map_to_vgc(config):
    '''
    '''
    # Determine CHIRP csv length
    # Divide CHIRP in 32 row chunks to comform to VGC max memory per channel group
    # Generate a VGC memory channel group from each <=32 row chunk
    # Perform necessary conversions for all Column data
    # write each VGC memory group to filename with appended number
    vgc_template = create_vgc_df()
    vgc_template['title'] = config['Name']
    vgc_template['rx_freq'] = config['Frequency'] * 1000000
    vgc_template['rx_freq'] = vgc_template['rx_freq'].astype(np.int64)
    vgc_template['rx_sub_audio(CTCSS=freq/DCS=number)'] = 0
    #Need to create logic to merge tones, replacing default values and map
    vgc_template['tx_sub_audio(CTCSS=freq/DCS=number)'] = config['rToneFreq'] + config['DtcsCode']
    #Logic to map CHIRP power to TX power
    vgc_template['tx_power(H/M/L)'] = 'H'
    #Figure out what this means and map accordingly 
    vgc_template['bandwidth(12500/25000)'] = 25000
    vgc_template['scan(0=OFF/1=ON)'] = 0
    vgc_template['talk around(0=OFF/1=ON)'] = 0
    vgc_template['pre_de_emph_bypass(0=OFF/1=ON)'] = 0
    vgc_template['sign(0=OFF/1=ON)'] = 1
    vgc_template['tx_dis(0=OFF/1=ON)'] = 1
    vgc_template['mute(0=OFF/1=ON)'] = 0
    #Map the following accordingly
    vgc_template['rx_modulation(0=FM/1=AM)'] = 0
    vgc_template['tx_modulation(0=FM/1=AM)'] = 0
    #print(config.iloc[50:84,0:10])
    print(vgc_template.iloc[0:5, 0:5])

def main():
    args = parse_args()
    chirp_config = chirp_to_df(args.input)
    convert_config = map_to_vgc(chirp_config)
    
if __name__ == "__main__":
    main()