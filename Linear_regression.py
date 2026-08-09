def gradient_descent(m_now,b_now,df,L):
    m_gradient = 0 
    b_gradient = 0
    n = len(df)
    for i in range(n):
        x = df.iloc[i].study_hours
        y = df.iloc[i].exam_score
        m_gradient += -(2/n) * x * (y-(m_now*x+b_now))
        b_gradient += -(2/n)* (y-(m_now*x+b_now))

    m = m_now - L*m_gradient
    b = b_now - L*b_gradient
    return m,b
