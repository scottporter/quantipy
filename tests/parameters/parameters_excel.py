
# BASIC
# -----------------------------------------------------------------------------
PATH_BASIC = './tests/basic.xlsx'
XKEYS_BASIC = [
    'q2', 'q2b', 'q3', 'q4',
    ['q5_1', 'q5_2', 'q5_3', 'q5_4', 'q5_5', 'q5_6'],
    'q8', 'q9']
YKEYS_BASIC = ['@', 'gender', 'gender', 'locality']
VIEWS_BASIC = ['cbase', 'counts']
OPENS_BASIC = ['q8a', 'q9a']
CELLS_BASIC = 'counts'
WEIGHT_BASIC = None

tab_names = ('q2b', 'q3', 'FOLDER_4', 'q8', 'q9')
SHEET_PROPERTIES_BASIC = dict(
    [(tab, dict(alternate_bg=True)) for tab in tab_names])

tab_names = ('q2', 'Open Ends')
widths = {0: 15, 5: 5, 10: 40}
SHEET_PROPERTIES_BASIC.update(dict(
    [(tab, dict(column_width_specific=widths)) for tab in tab_names]))

SHEET_PROPERTIES_EXCEL_BASIC = dict(
    dummy_tests=True,
    stat_0_rep='-',
    column_width=10,
    column_width_label=20,
    column_width_frame=50,
    alternate_bg=False)

FORMATS_BASIC = dict(
    view_border_freq=None,
    view_border_net=None,
    bold_u_base_text=True,
    bold_base_text=True,
    bold_label=True,
    bold_y=True,
    font_size=8,
    font_color_u_base_text='#551A8B',
    font_color_u_base='#551A8B',
    font_color_base='#066B06',
    font_color_base_text='#066B06',
    bg_color_freq='yellow')


# COMPLEX 1
# -----------------------------------------------------------------------------
PATH_COMPLEX_0 = './tests/complex_0.xlsx'
PATH_COMPLEX_1 = './tests/complex_1.xlsx'
PATH_COMPLEX_2 = './tests/complex_2.xlsx'
PATH_COMPLEX_3 = './tests/complex_3.xlsx'

XKEYS_COMPLEX = ['q5_1', 'q4', 'gender', 'Wave']
YKEYS_COMPLEX = ['@', 'q4 > gender', 'q4 > gender > Wave', 'q5_1']
VIEWS_COMPLEX = [
    'cbase', 'cbase_gross', 'ebase', 'counts', 'c%', 'r%', 'counts_sum',
    'c%_sum']
OPENS_COMPLEX = ['RecordNo', 'gender', 'age', 'q8', 'q8a', 'q9', 'q9a']
WEIGHT_COMPLEX = 'weight_a'

VIEWS_COMPLEX_MAIN = [
    'x|f|x:|||cbase',
    'x|f|x:||weight_a|cbase',
    'x|f|x:|||cbase_gross',
    'x|f|x:||weight_a|cbase_gross',
    'x|f|x:|||ebase',
    'x|f|x:||weight_a|ebase',
    (
        'x|f|:||weight_a|counts',
        'x|f|:|y|weight_a|c%',
        'x|f|:|x|weight_a|r%',
        'x|t.props.Dim.80+@|:||weight_a|test'
    ),
    (
        'x|f.c:f|x[{1,2}],x[{4,5}],x[{4,5}-{1,2}]:||weight_a|NPS',
        'x|f.c:f|x[{1,2}],x[{4,5}],x[{4,5}-{1,2}]:|y|weight_a|NPS',
        'x|f.c:f|x[{1,2}],x[{4,5}],x[{4,5}-{1,2}]:|x|weight_a|NPS',
        'x|t.props.Dim.80+@|x[{1,2}],x[{4,5}],x[{4,5}-{1,2}]:||weight_a|test'
    ),
    (
        'x|f.c:f|x[{4,5}-{1,2}]:||weight_a|NPSonly',
        'x|f.c:f|x[{4,5}-{1,2}]:|y|weight_a|NPSonly',
        'x|f.c:f|x[{4,5}-{1,2}]:|x|weight_a|NPSonly',
        'x|t.props.Dim.80+@|x[{4,5}-{1,2}]:||weight_a|test'
    ),
    (
        'x|f|x[{1,2,3}]:||weight_a|No',
        'x|f|x[{1,2,3}]:|y|weight_a|No',
        'x|f|x[{1,2,3}]:|x|weight_a|No',
        'x|t.props.Dim.80+@|x[{1,2,3}]:||weight_a|test'
    ),
    (
        'x|f|x[{4,5,97}]:||weight_a|Yes',
        'x|f|x[{4,5,97}]:|y|weight_a|Yes',
        'x|f|x[{4,5,97}]:|x|weight_a|Yes',
        'x|t.props.Dim.80+@|x[{4,5,97}]:||weight_a|test'
    ),
    (
        'x|d.mean|x:||weight_a|stat',
        'x|t.means.Dim.80+@|x:||weight_a|test'
    ),
    'x|d.stddev|x:||weight_a|stat',
    'x|d.median|x:||weight_a|stat',
    'x|d.var|x:||weight_a|stat',
    'x|d.varcoeff|x:||weight_a|stat',
    'x|d.sem|x:||weight_a|stat',
    'x|d.lower_q|x:||weight_a|stat',
    'x|d.upper_q|x:||weight_a|stat',
    (
        'x|f.c:f|x:||weight_a|counts_sum',
        'x|f.c:f|x:|y|weight_a|c%_sum'
    )]

VIEWS_COMPLEX_WAVE = [
    'x|f|x:|||cbase',
    'x|f|x:||weight_a|cbase',
    'x|f|x:|||cbase_gross',
    'x|f|x:||weight_a|cbase_gross',
    'x|f|x:|||ebase',
    'x|f|x:||weight_a|ebase',
    (
        'x|f|x[{1,2}+],x[{4,5}+]*:||weight_a|BLOCK',
        'x|f|x[{1,2}+],x[{4,5}+]*:|y|weight_a|BLOCK',
        'x|f|x[{1,2}+],x[{4,5}+]*:|x|weight_a|BLOCK',
        'x|t.props.Dim.80+@|x[{1,2}+],x[{4,5}+]*:||weight_a|test'
    ),
    (
        'x|d.mean|x:||weight_a|stat',
        'x|t.means.Dim.80+@|x:||weight_a|test'
    ),
    'x|d.stddev|x:||weight_a|stat',
    'x|d.median|x:||weight_a|stat',
    'x|d.var|x:||weight_a|stat',
    'x|d.varcoeff|x:||weight_a|stat',
    'x|d.sem|x:||weight_a|stat',
    'x|d.lower_q|x:||weight_a|stat',
    'x|d.upper_q|x:||weight_a|stat',
    (
        'x|f.c:f|x:||weight_a|counts_sum',
        'x|f.c:f|x:|y|weight_a|c%_sum'
    )]

VIEWS_COMPLEX_ARRAY = [
    'x|f|x:|||cbase',
    'x|f|x:||weight_a|cbase',
    (
        'x|f|:||weight_a|counts',
        'x|f|:|y|weight_a|c%'
    ),
    (
        'x|f|x[{1,2,3}]:||weight_a|No',
        'x|f|x[{1,2,3}]:|y|weight_a|No'
    ),
    (
        'x|f|x[{4,5,97}]:||weight_a|Yes',
        'x|f|x[{4,5,97}]:|y|weight_a|Yes'
    ),
    (
        'x|f.c:f|x[{4,5}-{1,2}]:||weight_a|NPSonly',
        'x|f.c:f|x[{4,5}-{1,2}]:|y|weight_a|NPSonly'
    ),
    (
        'x|f.c:f|x[{1,2}],x[{4,5}],x[{4,5}-{1,2}]:||weight_a|NPS',
        'x|f.c:f|x[{1,2}],x[{4,5}],x[{4,5}-{1,2}]:|y|weight_a|NPS'
    ),
    'x|d.mean|x:||weight_a|stat',
    'x|d.stddev|x:||weight_a|stat',
    'x|d.median|x:||weight_a|stat',
    'x|d.var|x:||weight_a|stat',
    'x|d.varcoeff|x:||weight_a|stat',
    'x|d.sem|x:||weight_a|stat',
    'x|d.lower_q|x:||weight_a|stat',
    'x|d.upper_q|x:||weight_a|stat',
    (
        'x|f.c:f|x:||weight_a|counts_sum',
        'x|f.c:f|x:|y|weight_a|c%_sum'
    )]

VIEWS_COMPLEX_MEAN = [
    'x|f|x:|||cbase',
    'x|f|x:||weight_a|cbase',
    'x|d.mean|x:||weight_a|stat',
    'x|d.stddev|x:||weight_a|stat',
    'x|d.median|x:||weight_a|stat',
    'x|d.var|x:||weight_a|stat',
    'x|d.varcoeff|x:||weight_a|stat',
    'x|d.sem|x:||weight_a|stat',
    'x|d.lower_q|x:||weight_a|stat',
    'x|d.upper_q|x:||weight_a|stat']

SHEET_PROPERTIES_0 = dict(alternate_bg=True)

FORMATS_0 = dict(
    view_border_freq=None,
    view_border_net=None,
    view_border_block_net=None,
    view_border_block_expanded=None,
    text_h_align_data=1)

SHEET_PROPERTIES_1 = dict(
    alternate_bg=True,
    freq_0_rep=':',
    stat_0_rep='#',
    y_header_height=20,
    y_row_height=40,
    column_width=10,
    column_width_label=40,
    column_width_frame=50,
    row_height_label=15,
    arrow_color_high='#66023C',
    arrow_rep_high=u'\u219F',
    arrow_color_low='#3F0F69',
    arrow_rep_low=u'\u21A1')

VIEW_GROUPS_1 = dict(
    block_expanded_counts='freq',
    block_expanded_c_pct='freq',
    block_expanded_r_pct='freq',
    block_expanded_propstest='freq',
    block_net_counts='freq',
    block_net_c_pct='freq',
    block_net_r_pct='freq',
    block_net_propstest='freq')

FORMATS_1 = dict(bg_color_freq='gray')

IMAGE_1 = dict(
    img_name='logo',
    img_url='./quantipy/core/builds/excel/formats/logo/qplogo_invert.png',
    img_size=[110, 120],
    img_insert_x=4,
    img_insert_y=0,
    img_x_offset=3,
    img_y_offset=6)

DECIMALS_1 = 3

SHEET_PROPERTIES_2 = dict(dummy_tests=True, alternate_bg=True)

VIEW_GROUPS_2 = dict(r_pct='sum', stddev='base')

FORMATS_2 = dict(
    bold_label=True,
    bold_u_base_text=True,
    font_color_u_base_text='#808080',
    font_color_u_base='#808080',
    bold_base_text=True,
    font_color_base_text='#632523',
    font_color_base='#632523',
    bold_c_base_gross_text=True,
    bg_color_c_base_gross_text='yellow',
    font_color_c_base_gross_text='pink',
    bold_c_base_gross=False,
    bg_color_c_base_gross='gray',
    font_color_c_base_gross='yellow',
    italic_freq_text=True,
    font_color_freq_text='blue',
    font_color_freq='blue',
    view_border_freq=False,
    font_color_net_text='#FF0000',
    font_color_net='#FF0000',
    font_color_stat_text='#FF0000',
    font_color_stat='#FF0000',
    bg_color_sum_text='#333333',
    font_color_sum_text='#FFA500',
    italic_sum=True,
    bold_block_net_text=True,
    italic_block_expanded_text=True,
    italic_block_normal_text=False,
    bold_header_left=True,
    font_color_header_left='#FFFFFF',
    text_h_align_header_left=1,
    bg_color_header_left='#AF8272',
    bold_header_center=True,
    font_color_header_center='#FFFFFF',
    text_h_align_header_center=1,
    bg_color_header_center='#85AD6E',
    bold_header_title=True,
    font_color_header_title='#265E1A',
    text_h_align_header_title=1,
    bg_color_header_title='#DFF442',
    bold_notes=True,
    font_color_notes='#FF6DB8',
    text_h_align_notes=1,
    bg_color_notes='#6DFFFC',
    bold_mask_label=True,
    bg_color_mask_label='#BDB1D8',
    font_color_mask_label='#33A59E',
    font_name_mask_label='Calibri',
    font_size_mask_label=11,
    italic_mask_label=True,
    text_v_align_mask_label=1,
    text_h_align_mask_label=3)

ANNOTATIONS_2 = ['Ann. 1', 'Ann. 2', 'Ann. 3', 'Ann. 4']

SHEET_PROPERTIES_3 = dict(
    dummy_tests=True,
    alternate_bg=False,
    start_row=7,
    start_column=2,
    start_row_annotations=4,
    start_column_annotations=5)

VIEW_GROUPS_3 = dict(
    block_normal_counts='block_normal',
    block_normal_c_pct='block_normal',
    block_normal_r_pct='block_normal',
    block_normal_propstest='block_normal')

FORMATS_3 = {
    'bold_y': True,
    'bg_color_y': '#B9FFCC',
    'font_color_y': 'gray',
    'font_name_y': 'Courier',
    'font_size_y': 12,
    'italic_y': True,
    'text_v_align_y': 3,
    'text_h_align_y': 1,
    'bold_label': True,
    'bg_color_label': 'red',
    'font_color_label': '#FFB6C1',
    'font_name_label': 'Calibri',
    'font_size_label': 11,
    'italic_label': True,
    'text_v_align_label': 1,
    'text_h_align_label': 3,
    'bold_u_c_base_text': True,
    'bg_color_u_c_base_text': 'green',
    'font_color_u_c_base_text': '#AB94FF',
    'font_name_u_c_base_text': 'Helvetica',
    'font_size_u_c_base_text': 11,
    'italic_u_c_base_text': True,
    'text_v_align_u_c_base_text': 3,
    'text_h_align_u_c_base_text': 2,
    'bold_u_c_base': True,
    'bg_color_u_c_base': '#AB94FF',
    'font_color_u_c_base': 'green',
    'font_name_u_c_base': 'Helvetica',
    'font_size_u_c_base': 11,
    'italic_u_c_base': True,
    'text_v_align_u_c_base': 3,
    'text_h_align_u_c_base': 3,
    'bold_c_base_text': True,
    'bg_color_c_base_text': '#AB94FF',
    'font_color_c_base_text': 'green',
    'font_name_c_base_text': 'Broadway',
    'font_size_c_base_text': 10,
    'italic_c_base_text': True,
    'text_v_align_c_base_text': 1,
    'text_h_align_c_base_text': 1,
    'bold_c_base': True,
    'bg_color_c_base': 'green',
    'font_color_c_base': '#AB94FF',
    'font_name_c_base': 'Broadway',
    'font_size_c_base': 10,
    'italic_c_base': True,
    'text_v_align_c_base': 1,
    'text_h_align_c_base': 1,
    'bold_u_c_base_gross_text': True,
    'bg_color_u_c_base_gross_text': '#DAF7A6',
    'font_color_u_c_base_gross_text': '#7DCEA0',
    'font_name_u_c_base_gross_text': 'Helvetica',
    'font_size_u_c_base_gross_text': 11,
    'italic_u_c_base_gross_text': True,
    'text_v_align_u_c_base_gross_text': 3,
    'text_h_align_u_c_base_gross_text': 2,
    'bold_u_c_base_gross': True,
    'bg_color_u_c_base_gross': '#7DCEA0',
    'font_color_u_c_base_gross': '#DAF7A6',
    'font_name_u_c_base_gross': 'Helvetica',
    'font_size_u_c_base_gross': 11,
    'italic_u_c_base_gross': True,
    'text_v_align_u_c_base_gross': 3,
    'text_h_align_u_c_base_gross': 3,
    'bold_c_base_gross_text': True,
    'bg_color_c_base_gross_text': '#7DCEA0',
    'font_color_c_base_gross_text': '#DAF7A6',
    'font_name_c_base_gross_text': 'Broadway',
    'font_size_c_base_gross_text': 10,
    'italic_c_base_gross_text': True,
    'text_v_align_c_base_gross_text': 1,
    'text_h_align_c_base_gross_text': 1,
    'bold_c_base_gross': True,
    'bg_color_c_base_gross': '#DAF7A6',
    'font_color_c_base_gross': '#7DCEA0',
    'font_name_c_base_gross': 'Broadway',
    'font_size_c_base_gross': 10,
    'italic_c_base_gross': True,
    'text_v_align_c_base_gross': 1,
    'text_h_align_c_base_gross': 1,
    'bold_u_e_base_text': True,
    'bg_color_u_e_base_text': '#839192',
    'font_color_u_e_base_text': '#E5F315',
    'font_name_u_e_base_text': 'Helvetica',
    'font_size_u_e_base_text': 11,
    'italic_u_e_base_text': True,
    'text_v_align_u_e_base_text': 3,
    'text_h_align_u_e_base_text': 2,
    'bold_u_e_base': True,
    'bg_color_u_e_base': '#E5F315',
    'font_color_u_e_base': '#839192',
    'font_name_u_e_base': 'Helvetica',
    'font_size_u_e_base': 11,
    'italic_u_e_base': True,
    'text_v_align_u_e_base': 3,
    'text_h_align_u_e_base': 3,
    'bold_e_base_text': True,
    'bg_color_e_base_text': '#E5F315',
    'font_color_e_base_text': '#839192',
    'font_name_e_base_text': 'Broadway',
    'font_size_e_base_text': 10,
    'italic_e_base_text': True,
    'text_v_align_e_base_text': 1,
    'text_h_align_e_base_text': 1,
    'bold_e_base': True,
    'bg_color_e_base': '#839192',
    'font_color_e_base': '#E5F315',
    'font_name_e_base': 'Broadway',
    'font_size_e_base': 10,
    'italic_e_base': True,
    'text_v_align_e_base': 1,
    'text_h_align_e_base': 1,
    'bold_counts_text': True,
    'bg_color_counts_text': '#8B4513',
    'font_color_counts_text': '#CD853F',
    'font_name_counts_text': 'FreeSerif',
    'font_size_counts_text': 13,
    'italic_counts_text': True,
    'text_v_align_counts_text': 3,
    'text_h_align_counts_text': 3,
    'bold_counts': True,
    'bg_color_counts': '#CD853F',
    'font_color_counts': '#8B4513',
    'font_name_counts': 'FreeSerif',
    'font_size_counts': 12,
    'italic_counts': True,
    'text_v_align_counts': 3,
    'text_h_align_counts': 3,
    'bold_c_pct_text': True,
    'bg_color_c_pct_text': '#CD853F',
    'font_color_c_pct_text': '#8B4513',
    'font_name_c_pct_text': 'FreeSerif',
    'font_size_c_pct_text': 12,
    'italic_c_pct_text': True,
    'text_v_align_c_pct_text': 1,
    'text_h_align_c_pct_text': 1,
    'bold_c_pct': True,
    'bg_color_c_pct': '#8B4513',
    'font_color_c_pct': '#CD853F',
    'font_name_c_pct': 'FreeSerif',
    'font_size_c_pct': 13,
    'italic_c_pct': True,
    'text_v_align_c_pct': 1,
    'text_h_align_c_pct': 1,
    'bold_r_pct_text': True,
    'bg_color_r_pct_text': '#8B4513',
    'font_text_color_r_pct': '#CD853F',
    'font_text_name_r_pct': 'FreeSerif',
    'font_size_r_pct_text': 12,
    'it_textalic_r_pct': True,
    'text_v_align_r_pct_text': 1,
    'text_h_align_r_pct_text': 1,
    'bold_r_pct': True,
    'bg_color_r_pct': '#CD853F',
    'font_color_r_pct': '#8B4513',
    'font_name_r_pct': 'FreeSerif',
    'font_size_r_pct': 13,
    'italic_r_pct': True,
    'text_v_align_r_pct': 1,
    'text_h_align_r_pct': 1,
    'bold_propstest_text': True,
    'bg_color_propstest_text': '#98FB98',
    'font_color_propstest_text': '#7DCEA0',
    'font_name_propstest_text': 'Liberation Sans Narrow',
    'font_size_propstest_text': 11,
    'italic_propstest_text': True,
    'text_v_align_propstest_text': 1,
    'text_h_align_propstest_text': 1,
    'bold_propstest': True,
    'bg_color_propstest': '#7DCEA0',
    'font_color_propstest': '#98FB98',
    'font_name_propstest': 'Liberation Sans Narrow',
    'font_size_propstest': 10,
    'italic_propstest': True,
    'text_v_align_propstest': 1,
    'text_h_align_propstest': 3,
    'bold_net_counts_text': True,
    'bg_color_net_counts_text': '#B2DFEE',
    'font_color_net_counts_text': '#FF5733',
    'font_name_net_counts_text': 'Century Schoolbook L',
    'font_size_net_counts_text': 11,
    'italic_net_counts_text': True,
    'text_v_align_net_counts_text': 1,
    'text_h_align_net_counts_text': 1,
    'bold_net_counts': True,
    'bg_color_net_counts': '#B2DFEE',
    'font_color_net_counts': '#FF5733',
    'font_name_net_counts': 'Century Schoolbook L',
    'font_size_net_counts': 13,
    'italic_net_counts': True,
    'text_v_align_net_counts': 1,
    'text_h_align_net_counts': 1,
    'bold_net_c_pct_text': True,
    'bg_color_net_c_pct_text': '#FF5733',
    'font_color_net_c_pct_text': '#B2DFEE',
    'font_name_net_c_pct_text': 'Century Schoolbook L',
    'font_size_net_c_pct_text': 11,
    'italic_net_c_pct_text': True,
    'text_v_align_net_c_pct_text': 1,
    'text_h_align_net_c_pct_text': 1,
    'bold_net_c_pct': True,
    'bg_color_net_c_pct': '#FF5733',
    'font_color_net_c_pct': '#B2DFEE',
    'font_name_net_c_pct': 'Century Schoolbook L',
    'font_size_net_c_pct': 13,
    'italic_net_c_pct': True,
    'text_v_align_net_c_pct': 1,
    'text_h_align_net_c_pct': 1,
    'bold_net_r_pct_text': True,
    'bg_color_net_r_pct_text': '#B2DFEE',
    'font_color_net_r_pct_text': '#FF5733',
    'font_name_net_r_pct_text': 'Century Schoolbook L',
    'font_size_net_r_pct_text': 11,
    'italic_net_r_pct_text': True,
    'text_v_align_net_r_pct_text': 1,
    'text_h_align_net_r_pct_text': 1,
    'bold_net_r_pct': True,
    'bg_color_net_r_pct': '#B2DFEE',
    'font_color_net_r_pct': '#FF5733',
    'font_name_net_r_pct': 'Century Schoolbook L',
    'font_size_net_r_pct': 13,
    'italic_net_r_pct': True,
    'text_v_align_net_r_pct': 1,
    'text_h_align_net_r_pct': 1,
    'bold_net_propstest_text': True,
    'bg_color_net_propstest_text': '#FF5733',
    'font_color_net_propstest_text': '#B2DFEE',
    'font_name_net_propstest_text': 'Century Schoolbook L',
    'font_size_net_propstest_text': 11,
    'italic_net_propstest_text': True,
    'text_v_align_net_propstest_text': 1,
    'text_h_align_net_propstest_text': 1,
    'bold_net_propstest': True,
    'bg_color_net_propstest': '#FF5733',
    'font_color_net_propstest': '#B2DFEE',
    'font_name_net_propstest': 'Century Schoolbook L',
    'font_size_net_propstest': 13,
    'italic_net_propstest': True,
    'text_v_align_net_propstest': 1,
    'text_h_align_net_propstest': 1,
    'bold_block_calc_net_counts_text': True,
    'bg_color_block_calc_net_counts_text': '#839192',
    'font_color_block_calc_net_counts_text': '#F8C471F',
    'font_name_block_calc_net_counts_text': 'Century Schoolbook L',
    'font_size_block_calc_net_counts_text': 11,
    'italic_block_calc_net_counts_text': True,
    'text_v_align_block_calc_net_counts_text': 1,
    'text_h_align_block_calc_net_counts_text': 1,
    'bold_block_calc_net_counts': True,
    'bg_color_block_calc_net_counts': '#F8C471F',
    'font_color_block_calc_net_counts': '#839192',
    'font_name_block_calc_net_counts': 'Century Schoolbook L',
    'font_size_block_calc_net_counts': 13,
    'italic_block_calc_net_counts': True,
    'text_v_align_block_calc_net_counts': 1,
    'text_h_align_block_calc_net_counts': 1,
    'bold_block_calc_net_c_pct_text': True,
    'bg_color_block_calc_net_c_pct_text': '#F8C471F',
    'font_color_block_calc_net_c_pct_text': '#839192',
    'font_name_block_calc_net_c_pct_text': 'Century Schoolbook L',
    'font_size_block_calc_net_c_pct_text': 11,
    'italic_block_calc_net_c_pct_text': True,
    'text_v_align_block_calc_net_c_pct_text': 1,
    'text_h_align_block_calc_net_c_pct_text': 1,
    'bold_block_calc_net_c_pct': True,
    'bg_color_block_calc_net_c_pct': '#839192',
    'font_color_block_calc_net_c_pct': '#F8C471F',
    'font_name_block_calc_net_c_pct': 'Century Schoolbook L',
    'font_size_block_calc_net_c_pct': 13,
    'italic_block_calc_net_c_pct': True,
    'text_v_align_block_calc_net_c_pct': 1,
    'text_h_align_block_calc_net_c_pct': 1,
    'bold_block_calc_net_r_pct_text': True,
    'bg_color_block_calc_net_r_pct_text': '#839192',
    'font_color_block_calc_net_r_pct_text': '#F8C471F',
    'font_name_block_calc_net_r_pct_text': 'Century Schoolbook L',
    'font_size_block_calc_net_r_pct_text': 11,
    'italic_block_calc_net_r_pct_text': True,
    'text_v_align_block_calc_net_r_pct_text': 1,
    'text_h_align_block_calc_net_r_pct_text': 1,
    'bold_block_calc_net_r_pct': True,
    'bg_color_block_calc_net_r_pct': '#F8C471F',
    'font_color_block_calc_net_r_pct': '#839192',
    'font_name_block_calc_net_r_pct': 'Century Schoolbook L',
    'font_size_block_calc_net_r_pct': 13,
    'italic_block_calc_net_r_pct': True,
    'text_v_align_block_calc_net_r_pct': 1,
    'text_h_align_block_calc_net_r_pct': 1,
    'bold_block_calc_net_propstest_text': True,
    'bg_color_block_calc_net_propstest_text': '#F8C471F',
    'font_color_block_calc_net_propstest_text': '#839192',
    'font_name_block_calc_net_propstest_text': 'Century Schoolbook L',
    'font_size_block_calc_net_propstest_text': 11,
    'italic_block_calc_net_propstest_text': True,
    'text_v_align_block_calc_net_propstest_text': 1,
    'text_h_align_block_calc_net_propstest_text': 1,
    'bold_block_calc_net_propstest': True,
    'bg_color_block_calc_net_propstest': '#839192',
    'font_color_block_calc_net_propstest': '#F8C471F',
    'font_name_block_calc_net_propstest': 'Century Schoolbook L',
    'font_size_block_calc_net_propstest': 13,
    'italic_block_calc_net_propstest': True,
    'text_v_align_block_calc_net_propstest': 1,
    'text_h_align_block_calc_net_propstest': 1,
    'bold_block_calc_counts_text': True,
    'bg_color_block_calc_counts_text': 'blue',
    'font_color_block_calc_counts_text': 'red',
    'font_name_block_calc_counts_text': 'Century Schoolbook L',
    'font_size_block_calc_counts_text': 11,
    'italic_block_calc_counts_text': True,
    'text_v_align_block_calc_counts_text': 1,
    'text_h_align_block_calc_counts_text': 1,
    'bold_block_calc_counts': True,
    'bg_color_block_calc_counts': 'red',
    'font_color_block_calc_counts': 'blue',
    'font_name_block_calc_counts': 'Century Schoolbook L',
    'font_size_block_calc_counts': 13,
    'italic_block_calc_counts': True,
    'text_v_align_block_calc_counts': 1,
    'text_h_align_block_calc_counts': 1,
    'bold_block_calc_c_pct_text': True,
    'bg_color_block_calc_c_pct_text': 'red',
    'font_color_block_calc_c_pct_text': 'blue',
    'font_name_block_calc_c_pct_text': 'Century Schoolbook L',
    'font_size_block_calc_c_pct_text': 11,
    'italic_block_calc_c_pct_text': True,
    'text_v_align_block_calc_c_pct_text': 1,
    'text_h_align_block_calc_c_pct_text': 1,
    'bold_block_calc_c_pct': True,
    'bg_color_block_calc_c_pct': 'blue',
    'font_color_block_calc_c_pct': 'red',
    'font_name_block_calc_c_pct': 'Century Schoolbook L',
    'font_size_block_calc_c_pct': 13,
    'italic_block_calc_c_pct': True,
    'text_v_align_block_calc_c_pct': 1,
    'text_h_align_block_calc_c_pct': 1,
    'bold_block_calc_r_pct_text': True,
    'bg_color_block_calc_r_pct_text': 'blue',
    'font_color_block_calc_r_pct_text': 'red',
    'font_name_block_calc_r_pct_text': 'Century Schoolbook L',
    'font_size_block_calc_r_pct_text': 11,
    'italic_block_calc_r_pct_text': True,
    'text_v_align_block_calc_r_pct_text': 1,
    'text_h_align_block_calc_r_pct_text': 1,
    'bold_block_calc_r_pct': True,
    'bg_color_block_calc_r_pct': 'red',
    'font_color_block_calc_r_pct': 'blue',
    'font_name_block_calc_r_pct': 'Century Schoolbook L',
    'font_size_block_calc_r_pct': 13,
    'italic_block_calc_r_pct': True,
    'text_v_align_block_calc_r_pct': 1,
    'text_h_align_block_calc_r_pct': 1,
    'bold_block_calc_propstest_text': True,
    'bg_color_block_calc_propstest_text': 'red',
    'font_color_block_calc_propstest_text': 'blue',
    'font_name_block_calc_propstest_text': 'Century Schoolbook L',
    'font_size_block_calc_propstest_text': 11,
    'italic_block_calc_propstest_text': True,
    'text_v_align_block_calc_propstest_text': 1,
    'text_h_align_block_calc_propstest_text': 1,
    'bold_block_calc_propstest': True,
    'bg_color_block_calc_propstest': 'blue',
    'font_color_block_calc_propstest': 'red',
    'font_name_block_calc_propstest': 'Century Schoolbook L',
    'font_size_block_calc_propstest': 13,
    'italic_block_calc_propstest': True,
    'text_v_align_block_calc_propstest': 1,
    'text_h_align_block_calc_propstest': 1,
    'bold_block_net_text': True,
    'bg_color_block_net_text': '#15F3BB',
    'font_color_block_net_text': '#F31588',
    'font_name_block_net_text': 'Century Schoolbook L',
    'font_size_block_net_text': 11,
    'italic_block_net_text': True,
    'text_v_align_block_net_text': 1,
    'text_h_align_block_net_text': 1,
    'bold_block_net': True,
    'bg_color_block_net': '#F31588',
    'font_color_block_net': '#15F3BB',
    'font_name_block_net': 'Century Schoolbook L',
    'font_size_block_net': 13,
    'italic_block_net': True,
    'text_v_align_block_net': 1,
    'text_h_align_block_net': 1,
    'bold_block_expanded_text': True,
    'bg_color_block_expanded_text': '#F08080',
    'font_color_block_expanded_text': '#FCF3CF',
    'font_name_block_expanded_text': 'Century Schoolbook L',
    'font_size_block_expanded_text': 11,
    'italic_block_expanded_text': True,
    'text_v_align_block_expanded_text': 1,
    'text_h_align_block_expanded_text': 1,
    'bold_block_expanded': True,
    'bg_color_block_expanded': '#FCF3CF',
    'font_color_block_expanded': '#F08080',
    'font_name_block_expanded': 'Century Schoolbook L',
    'font_size_block_expanded': 13,
    'italic_block_expanded': True,
    'text_v_align_block_expanded': 1,
    'text_h_align_block_expanded': 1,
    'bold_block_normal_text': True,
    'bg_color_block_normal_text': '#00BFFF',
    'font_color_block_normal_text': '#F08080',
    'font_name_block_normal_text': 'Century Schoolbook L',
    'font_size_block_normal_text': 11,
    'italic_block_normal_text': True,
    'tnormalign_block_expanded_text': 1,
    'tnormalign_block_expanded_text': 1,
    'bold_block_normal': True,
    'bg_color_block_normal': '#F08080',
    'font_color_block_normal': '#00BFFF',
    'font_name_block_normal': 'Century Schoolbook L',
    'font_size_block_normal': 13,
    'italic_block_normal': True,
    'text_v_align_block_normal': 1,
    'text_h_align_block_normal': 1,
    'bold_mean_text': True,
    'bg_color_mean_text': '#FF69B4',
    'font_color_mean_text': '#00E5EE',
    'font_name_mean_text': 'MathJax_SanSerif',
    'font_size_mean_text': 13,
    'italic_mean_text': True,
    'text_v_align_mean_text': 3,
    'text_h_align_mean_text': 3,
    'bold_mean': True,
    'bg_color_mean': '#FF69B4',
    'font_color_mean': '#00E5EE',
    'font_name_mean': 'MathJax_SanSerif',
    'font_size_mean': 11,
    'italic_mean': True,
    'text_v_align_mean': 3,
    'text_h_align_mean': 3,
    'bold_stddev_text': True,
    'bg_color_stddev_text': '#FF69B4',
    'font_color_stddev_text': '#00E5EE',
    'font_name_stddev_text': 'MathJax_SanSerif',
    'font_size_stddev_text': 13,
    'italic_stddev_text': True,
    'text_v_align_stddev_text': 3,
    'text_h_align_stddev_text': 3,
    'bold_stddev': True,
    'bg_color_stddev': '#FF69B4',
    'font_color_stddev': '#00E5EE',
    'font_name_stddev': 'MathJax_SanSerif',
    'font_size_stddev': 11,
    'italic_stddev': True,
    'text_v_align_stddev': 3,
    'text_h_align_stddev': 3,
    'bold_median_text': True,
    'bg_color_median_text': '#FF69B4',
    'font_color_median_text': '#00E5EE',
    'font_name_median_text': 'MathJax_SanSerif',
    'font_size_median_text': 13,
    'italic_median_text': True,
    'text_v_align_median_text': 3,
    'text_h_align_median_text': 3,
    'bold_median': True,
    'bg_color_median': '#FF69B4',
    'font_color_median': '#00E5EE',
    'font_name_median': 'MathJax_SanSerif',
    'font_size_median': 11,
    'italic_median': True,
    'text_v_align_median': 3,
    'text_h_align_median': 3,
    'bold_var_text': True,
    'bg_color_var_text': '#FF69B4',
    'font_color_var_text': '#00E5EE',
    'font_name_var_text': 'MathJax_SanSerif',
    'font_size_var_text': 13,
    'italic_var_text': True,
    'text_v_align_var_text': 3,
    'text_h_align_var_text': 3,
    'bold_var': True,
    'bg_color_var': '#FF69B4',
    'font_color_var': '#00E5EE',
    'font_name_var': 'MathJax_SanSerif',
    'font_size_var': 11,
    'italic_var': True,
    'text_v_align_var': 3,
    'text_h_align_var': 3,
    'bold_varcoeff_text': True,
    'bg_color_varcoeff_text': '#FF69B4',
    'font_color_varcoeff_text': '#00E5EE',
    'font_name_varcoeff_text': 'MathJax_SanSerif',
    'font_size_varcoeff_text': 13,
    'italic_varcoeff_text': True,
    'text_v_align_varcoeff_text': 3,
    'text_h_align_varcoeff_text': 3,
    'bold_varcoeff': True,
    'bg_color_varcoeff': '#FF69B4',
    'font_color_varcoeff': '#00E5EE',
    'font_name_varcoeff': 'MathJax_SanSerif',
    'font_size_varcoeff': 11,
    'italic_varcoeff': True,
    'text_v_align_varcoeff': 3,
    'text_h_align_varcoeff': 3,
    'bold_sem_text': True,
    'bg_color_sem_text': '#FF69B4',
    'font_color_sem_text': '#00E5EE',
    'font_name_sem_text': 'MathJax_SanSerif',
    'font_size_sem_text': 13,
    'italic_sem_text': True,
    'text_v_align_sem_text': 3,
    'text_h_align_sem_text': 3,
    'bold_sem': True,
    'bg_color_sem': '#FF69B4',
    'font_color_sem': '#00E5EE',
    'font_name_sem': 'MathJax_SanSerif',
    'font_size_sem': 11,
    'italic_sem': True,
    'text_v_align_sem': 3,
    'text_h_align_sem': 3,
    'bold_lower_q_text': True,
    'bg_color_lower_q_text': '#FF69B4',
    'font_color_lower_q_text': '#FFFF00',
    'font_name_lower_q_text': 'MathJax_SanSerif',
    'font_size_lower_q_text': 13,
    'italic_lower_q_text': True,
    'text_v_align_lower_q_text': 3,
    'text_h_align_lower_q_text': 3,
    'bold_lower_q': True,
    'bg_color_lower_q': '#FF69B4',
    'font_color_lower_q': '#00E5EE',
    'font_name_lower_q': 'MathJax_SanSerif',
    'font_size_lower_q': 11,
    'italic_lower_q': True,
    'text_v_align_lower_q': 3,
    'text_h_align_lower_q': 3,
    'bold_upper_q_text': True,
    'bg_color_upper_q_text': '#FF69B4',
    'font_color_upper_q_text': '#00E5EE',
    'font_name_upper_q_text': 'MathJax_SanSerif',
    'font_size_upper_q_text': 13,
    'italic_upper_q_text': True,
    'text_v_align_upper_q_text': 3,
    'text_h_align_upper_q_text': 3,
    'bold_upper_q': True,
    'bg_color_upper_q': '#FF69B4',
    'font_color_upper_q': '#00E5EE',
    'font_name_upper_q': 'MathJax_SanSerif',
    'font_size_upper_q': 11,
    'italic_upper_q': True,
    'text_v_align_upper_q': 3,
    'text_h_align_upper_q': 3,
    'bold_meanstest_text': True,
    'bg_color_meanstest_text': '#00E5EE',
    'font_color_meanstest_text': '#FF69B4',
    'font_name_meanstest_text': 'MathJax_SanSerif',
    'font_size_meanstest_text': 11,
    'italic_meanstest_text': True,
    'text_v_align_meanstest_text': 3,
    'text_h_align_meanstest_text': 3,
    'bold_meanstest': True,
    'bg_color_meanstest': '#00E5EE',
    'font_color_meanstest': '#FF69B4',
    'font_name_meanstest': 'MathJax_SanSerif',
    'font_size_meanstest': 13,
    'italic_meanstest': True,
    'text_v_align_meanstest': 3,
    'text_h_align_meanstest': 3,
    'bold_counts_sum_text': True,
    'bg_color_counts_sum_text': '#34495E',
    'font_color_counts_sum_text': '#D4AC0D',
    'font_name_counts_sum_text': 'URW Gothic L',
    'font_size_counts_sum_text': 8,
    'italic_counts_sum_text': True,
    'text_v_align_counts_sum_text': 1,
    'text_h_align_counts_sum_text': 1,
    'bold_counts_sum': True,
    'bg_color_counts_sum': '#34495E',
    'font_color_counts_sum': '#D4AC0D',
    'font_name_counts_sum': 'URW Gothic L',
    'font_size_counts_sum': 10,
    'italic_counts_sum': True,
    'text_v_align_counts_sum': 1,
    'text_h_align_counts_sum': 3,
    'bold_c_pct_sum_text': True,
    'bg_color_c_pct_sum_text': '#D4AC0D',
    'font_color_c_pct_sum_text': '#34495E',
    'font_name_c_pct_sum_text': 'URW Gothic L',
    'font_size_c_pct_sum_text': 8,
    'italic_c_pct_sum_text': True,
    'text_v_align_c_pct_sum_text': 1,
    'text_h_align_c_pct_sum_text': 1,
    'bold_c_pct_sum': True,
    'bg_color_c_pct_sum': '#D4AC0D',
    'font_color_c_pct_sum': '#34495E',
    'font_name_c_pct_sum': 'URW Gothic L',
    'font_size_c_pct_sum': 10,
    'italic_c_pct_sum': True,
    'text_v_align_c_pct_sum': 1,
    'text_h_align_c_pct_sum': 3}

annotations_spec = (
    (
        'Main',
        [
            (
                'Main. 1',
                dict(font_size=8, font_color='yellow', bg_color='gray')
            ),
            (
                'Main. 2',
                dict(
                    font_size=10,
                    font_color='green',
                    bg_color='gray',
                    bold=True)
            ),
            (
                'Main. 3',
                dict(
                    font_size=12,
                    font_color='blue',
                    bg_color='gray',
                    italic=True)
            ),
            (
                'Main. 4',
                dict(font_size=14, font_color='pink', bg_color='gray')
            )
        ],
    ),
    ('arr_0', ['Arr.0 0 - loooooooooooong - to test text wrapping']),
    ('arr_1', ['Arr.1 1', 'Arr.1 1']),
    ('mean_0', ['Mean.0 1', 'Mean.0 1', 'Mean.0 2']),
    ('mean_1', ['Mean.1 1', 'Mean.1 2', 'Mean.1 3', 'Mean.1 4']),
    ('Open Ends', ['A', 'B', 'C', 'D', 'E', 'F']))

ANNOTATIONS_3 = dict([_ for _ in annotations_spec])

ITALICISE_LEVEL_3 = 50

DECIMALS_3 = dict(N=0, P=2, D=1)

DETAILS_3 = True
