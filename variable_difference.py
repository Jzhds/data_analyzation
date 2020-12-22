# 在分类问题上，看不同类型的数据在不同类别上面的分布情况的差异，进而选出来哪些变量会对预测有比较好的作用，具体包括连续变量（画箱线图以及比较平均数是否有显著差异），
# 分类变量（通过画饼图看分布是否有明显差异）
def test_for_categorial_variable(column_name,sort=True,counts_sort=False):
    df_attritions_column_name = df_attritions[f'{column_name}'].value_counts(sort=counts_sort)
    df_attritions_column_name = pd.DataFrame({f'{column_name}': df_attritions_column_name.index, 'count': df_attritions_column_name.values})

    # Taking the count of each Sex value inside the Survivors
    df_nonattritions_column_name= df_nonattritions[f'{column_name}'].value_counts(sort=counts_sort)
    df_nonattritions_column_name = pd.DataFrame({f'{column_name}': df_nonattritions_column_name.index, 'count': df_nonattritions_column_name.values})

    # Creating the plotting objects
    pie_survivors_column_name = go.Pie(
        labels=df_attritions_column_name[f'{column_name}'],
        values=df_attritions_column_name['count'],
        domain=dict(x=[0, 0.5]),
        name='attritions',
        hole=0.5,
       # marker=dict(colors=['violet', 'cornflowerblue'], line=dict(color='#000000', width=2)),
        sort = sort
    )

    pie_nonsurvivors_column_name = go.Pie(
        labels=df_nonattritions_column_name[f'{column_name}'],
        values=df_nonattritions_column_name['count'],
        domain=dict(x=[0.5, 1.0]),
        name='non-attritions',
        hole=0.5,
        #marker=dict(colors=['violet', 'cornflowerblue'], line=dict(color='#000000', width=2)),
        sort = sort
    )

    data = [pie_survivors_column_name, pie_nonsurvivors_column_name]

    # Plot's Layout (background color, title, annotations, etc.)
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=f'"{column_name}" percentage from Attritions vs non-Attritions',
        annotations=[dict(text='Attritions', x=0.18, y=0.5, font_size=15, showarrow=False),
                     dict(text='Non-Attritions', x=0.85, y=0.5, font_size=15, showarrow=False)]
    )

    fig = go.Figure(data=data, layout=layout)

    fig.show()
   
   
def test_for_continous_variable( column_name ):
    violin_attritions = go.Violin(
        y=df_attritions[f'{column_name}'],
        x=df_attritions['Attrition'],
        name='Attritions',
        marker_color='forestgreen',
        box_visible=True)

    violin_nonattritions = go.Violin(
        y=df_nonattritions[f'{column_name}'],
        x=df_nonattritions['Attrition'],
        name='Non-attritions',
        marker_color='darkred',
        box_visible=True)

    data = [violin_attritions, violin_nonattritions]

    # Plot's Layout (background color, title, etc.)
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=f'{column_name} of attritions vs {column_name} of non-attritions',
        xaxis=dict(
            title='Attrition or not'
        ),
        yaxis=dict(
            title=f'{column_name}'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    fig.show()

    dist_a = df_attritions[f'{column_name}']
    dist_b = df_nonattritions[f'{column_name}']
    t_stat, p_value = ztest(dist_a, dist_b)
    print(column_name)
    print("----- Z Test Results -----")
    print("T stat. = " + str(t_stat))
    print("P value = " + str(p_value))  # P-value is less than 0.05

    print("")

    t_stat_2, p_value_2 = stats.ttest_ind(dist_a, dist_b)
    print("----- T Test Results -----")
    print("T stat. = " + str(t_stat_2))
    print("P value = " + str(p_value_2))
