from numpy.random import random, normal

def Get_Random_First_Names(rows=1):
    first_names = [
        James, Mary,
        John, Patricia,
        Robert, Jennifer,
        Michael, Linda,
        William, Elizabeth,
        David, Barbara,
        Richard, Susan,
        Joseph, Jessica,
        Thomas, Sarah,
        Charles, Karen,
        Christopher, Nancy,
        Daniel, Margaret,
        Matthew, Lisa,
        Anthony, Betty,
        Donald, Dorothy,
        Mark, Sandra,
        Paul, Ashley,
        Steven, Kimberly,
        Andrew, Donna,
        Kenneth, Emily,
        Joshua, Michelle,
        George, Carol,
        Kevin, Amanda,
        Brian, Melissa,
        Edward, Deborah,
        Ronald, Stephanie,
        Timothy, Rebecca,
        Jason, Laura,
        Jeffrey, Sharon,
        Ryan, Cynthia,
        Jacob, Kathleen,
        Gary, Helen,
        Nicholas, Amy,
        Eric, Shirley,
        Stephen, Angela,
        Jonathan, Anna,
        Larry, Brenda,
        Justin, Pamela,
        Scott, Nicole,
        Brandon, Ruth,
        Frank, Katherine,
        Benjamin, Samantha,
        Gregory, Christine,
        Samuel, Emma,
        Raymond, Catherine,
        Patrick, Debra,
        Alexander, Virginia,
        Jack, Rachel,
        Dennis, Carolyn,
        Jerry, Janet,
        Tyler, Maria,
        Aaron, Heather,
        Jose, Diane,
        Henry, Julie,
        Douglas, Joyce,
        Adam, Victoria,
        Peter, Kelly,
        Nathan, Christina,
        Zachary, Joan,
        Walter, Evelyn,
        Kyle, Lauren,
        Harold, Judith,
        Carl, Olivia,
        Jeremy, Frances,
        Keith, Martha,
        Roger, Cheryl,
        Gerald, Megan,
        Ethan, Andrea,
        Arthur, Hannah,
        Terry, Jacqueline,
        Christian, Ann,
        Sean, Jean,
        Lawrence, Alice,
        Austin, Kathryn,
        Joe, Gloria,
        Noah, Teresa,
        Jesse, Doris,
        Albert, Sara,
        Bryan, Janice,
        Billy, Julia,
        Bruce, Marie,
        Willie, Madison,
        Jordan, Grace,
        Dylan, Judy,
        Alan, Theresa,
        Ralph, Beverly,
        Gabriel, Denise,
        Roy, Marilyn,
        Juan, Amber,
        Wayne, Danielle,
        Eugene, Abigail,
        Logan, Brittany,
        Randy, Rose,
        Louis, Diana,
        Russell, Natalie,
        Vincent, Sophia,
        Philip, Alexis,
        Bobby, Lori,
        Johnny, Kayla,
        Bradley, Jane,
        ]
    name_count = len(first_names) - 1
    random_list_numbers = name_count * random(rows)
    random_first_names = []
    [random_first_names.append(first_names[int(rand_num)]) \
        for rand_num in random_list_numbers]
    return random_first_names


def Get_Random_Last_Names(rows=1):
    last_names = [
        SMITH, JOHNSON, WILLIAMS, BROWN,
        JONES, GARCIA, MILLER, DAVIS,
        RODRIGUEZ, MARTINEZ, HERNANDEZ, LOPEZ,
        GONZALEZ, WILSON, ANDERSON, THOMAS,
        TAYLOR, MOORE, JACKSON, MARTIN,
        LEE, PEREZ, THOMPSON, WHITE,
        HARRIS, SANCHEZ, CLARK, RAMIREZ,
        LEWIS, ROBINSON, WALKER, YOUNG,
        ALLEN, KING, WRIGHT, SCOTT,
        TORRES, NGUYEN, HILL, FLORES,
        GREEN, ADAMS, NELSON, BAKER,
        HALL, RIVERA, CAMPBELL, MITCHELL,
        CARTER, ROBERTS, GOMEZ, PHILLIPS,
        EVANS, TURNER, DIAZ, PARKER,
        CRUZ, EDWARDS, COLLINS, REYES,
        STEWART, MORRIS, MORALES, MURPHY,
        COOK, ROGERS, GUTIERREZ, ORTIZ,
        MORGAN, COOPER, PETERSON, BAILEY,
        REED, KELLY, HOWARD, RAMOS,
        KIM, COX, WARD, RICHARDSON,
        WATSON, BROOKS, CHAVEZ, WOOD,
        JAMES, BENNETT, GRAY, MENDOZA,
        RUIZ, HUGHES, PRICE, ALVAREZ,
        CASTILLO, SANDERS, PATEL, MYERS,
        LONG, ROSS, FOSTER, JIMENEZ,
        POWELL, JENKINS, PERRY, RUSSELL,
        SULLIVAN, BELL, COLEMAN, BUTLER,
        HENDERSON, BARNES,
        ]
    name_count = len(last_names) - 1
    random_list_numbers = name_count * random(rows)
    random_last_names = []
    [random_last_names.append(last_names[int(rand_num)]) \
        for rand_num in random_list_numbers]
    return random_last_names

def Get_Random_Scores(rows=1, mean=0.75, stddev=0.3, max_value=100):
    ''' Normal Distribution List. '''
    normal_list = normal(mean, stddev, rows) * max_value
    random_scores = []
    for normal_value in normal_list:
        if normal_value > max_value:
            normal_value = max_value
        elif normal_value < 0:
            normal_value = 0
        random_scores.append(normal_value)
    return random_scores



