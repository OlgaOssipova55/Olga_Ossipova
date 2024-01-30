import pandas as pd

#Задание 1
data = {
    'Name': ['Алексей', 'Мария', 'Иван', 'Екатерина'],
    'Age': [20, 21, 19, 22],
    'Gender': ['М', 'Ж', 'М', 'Ж'],
    'GPA': [3.5, 4.0, 3.2, 3.8]
}

student_df = pd.DataFrame(data)

print(student_df)

#Задание 2
female_students_names = student_df.loc[student_df['Gender'] == 'Ж', 'Name']
print(female_students_names)

top_student = student_df[student_df['GPA'] == student_df['GPA'].max()]
print(top_student)

#Задание 3
student_df['Age'] = student_df['Age'] + 1

min_age = student_df['Age'].min()
student_df.loc[student_df['Age'] == min_age, 'GPA'] = student_df['GPA'] + 0.5

print(student_df)

# Задание 4
new_student_data = {
    'Name': 'Elena',
    'Age': 20,
    'Gender': 'Female',
    'Major': 'Computer Science',
    'GPA': 3.8
}

new_student_df = pd.DataFrame([new_student_data])
student_df = pd.concat([student_df, new_student_df], ignore_index=True)

print(student_df)


#Задание 5 
student_df['GPA'] = student_df['GPA'] + 0.5

print(student_df)

# Задание 6
student_df_sorted_by_age = student_df.sort_values(by='Age', ascending=False)
print("Сортировка студентов по возрасту (по убыванию):")
print(student_df_sorted_by_age)

student_df_sorted_by_gpa = student_df.sort_values(by='GPA', ascending=True)
print("\nСортировка студентов по GPA (по возрастанию):")
print(student_df_sorted_by_gpa)

# Задание 7
student_df.to_csv('student_records.csv', index=False) 
