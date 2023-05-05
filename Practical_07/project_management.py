"""
time estimate: 1 hours
start time: 4:23 pm
end time: 6 am morning
"""

from project import ProjectManagement


def main():
    """the project management for storing, updating the project information"""
    print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")
    data = load_file('projects.txt')
    projects = add_object(data)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input('Filename: ')
            if filename != '':
                try:
                    data = load_file(filename)
                    projects = add_object(data)
                except FileNotFoundError:
                    print('Invalid Filename')
        elif choice == 'S':
            save_filename = input('Please enter the saved file: ')
            if save_filename != '':
                try:
                    save_file(data, save_filename)
                except FileNotFoundError:
                    print('Invalid Filename')
        elif choice == "D":
            complete_project, incomplete_project = group_completeproject(projects)
            print('Incomplete projects: ')
            incomplete_project.sort()
            display_project(incomplete_project, False)
            print('Completed projects: ')
            complete_project.sort()
            display_project(complete_project, False)
        elif choice == 'F':
            date = input('Show projects that start after date (dd/mm/yy): ')
            filtered_projects = []
            for project in projects:
                if project.compare_date(date):
                    filtered_projects.append(project)
            filtered_projects = sort_projects(filtered_projects)
            display_project(filtered_projects, False)
        elif choice == "A":
            print('Lets add a new project')
            try:
                name = input('Name: ')
                start_date = input('Start date (dd/mm/yy): ')
                priority = int(input('Priority: '))
                cost_estimate = input('Cost estimate: ')
                cost_estimate = cost_estimate.replace('$', '')
                cost_estimate = int(cost_estimate)
                percent_complete = input('Percent complete: ')
                project = ProjectManagement(str(name), str(start_date), int(priority), int(cost_estimate),
                                            int(percent_complete))
                projects.append(project)
            except ValueError:
                print('Invalid Input')
        elif choice == 'U':
            projects = sort_projects(projects)
            display_project(projects, True)
            projects_data = {}
            for number, project in enumerate(projects):
                projects_data[str(number)] = project
            try:
                project_choice = input('Project choice: ')
                chosen_project = projects_data[project_choice]
                print(chosen_project)
                new_percentage = input('New Percentage: ')
                new_priority = input('New Priority: ')
                if new_percentage != '':
                    chosen_project.update_percentage(int(new_percentage))
                if new_priority != '':
                    chosen_project.update_priority(int(new_priority))
            except KeyError:
                print('Invalid Choice')
        else:
            print('Invalid choice!')
        print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")
        choice = input('>>> ').upper()
    print('Thank you for using custom-built project management software.')


def sort_projects(projects):
    """sort the project by date for display"""
    date_list = []
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
    date_list.sort()
    sorted_project = []
    for date in date_list:
        for number, project in enumerate(projects):
            if project.start_date == date:
                sorted_project.append(project)
    return sorted_project


def display_project(projects, order):
    """display the project:
    order: True display the project with index number
    order: False display the project without index number"""
    if order:
        for num, project in enumerate(projects):
            print(f'{num} {project}')
    else:
        for project in projects:
            print(project)


def group_completeproject(projects):
    """split the project into completed and incomplete projects"""
    completed_project = []
    incomplete_project = []
    for project in projects:
        if project.is_finished():
            completed_project.append(project)
            completed_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return completed_project, incomplete_project


def load_file(filename):
    """load the file data to a list of row"""
    projects = []
    in_file = open(filename, 'r')
    data = in_file.readlines()
    for line in data[1:]:
        slash_position = line.find('/')
        project_name = line[:slash_position - 3]
        project_detail = line[slash_position - 2:]
        project_detail = project_detail.split()
        project_data = [project_name] + project_detail
        projects.append(project_data)
    return projects


def save_file(data, filename):
    """save the data to the file as csv mode"""
    out_file = open(filename, 'w')
    print('Name	Start Date Priority	Cost Estimate	Completion Percentage', file=out_file)
    for line in data:
        line = ','.join(line)
        print(line, file=out_file)
    out_file.close()


def add_object(data):
    """convert the input data list to a list of project objects"""
    projects = []
    for line in data:
        project = ProjectManagement(line[0], line[1], line[2], line[3], line[4])
        projects.append(project)
    return projects


main()