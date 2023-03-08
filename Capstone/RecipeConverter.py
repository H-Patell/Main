#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def parse_fractions(ingredient):
    # From Genius recipes
    ingredient = ingredient.replace('1⁄4', '.25')
    ingredient = ingredient.replace('1⁄3', '.33')
    ingredient = ingredient.replace('1⁄2', '.5')
    ingredient = ingredient.replace('2⁄3', '.66')
    ingredient = ingredient.replace('3⁄4', '.75')
    
    ingredient = ingredient.replace('1/8', '.125')
    ingredient = ingredient.replace('1/4', '.25')
    ingredient = ingredient.replace('1/3', '.33')
    ingredient = ingredient.replace('1/2', '.5')
    ingredient = ingredient.replace('2/3', '.66')
    ingredient = ingredient.replace('3/4', '.75')
    
    return ingredient

def get_conversion(line):
    if 'butter' in line and 'cup' in line:
        output =  parse_ingredient_line(line, 227)
        
    return output

def convert_ingredient(line, unit, conversion):
    # Extract number from measurement
    number_string = line.split(unit)[0].replace(' ','')
    if not number_string:
        number_string = 1
    number_float = float(number_string)

    # Convert butter cup to grams
    converted = number_float * conversion

    # Construct the output ingredient line with original line
    line_out = '%.1f g%s'%(converted, line.split(unit)[1].strip('s'))
    return line_out

def parse_recipe(df_ing_quant):
    output = {}
    for i in range(0, df_ing_quant.shape[0]):
        ingredient = df_ing_quant["Ingredient"][i]
        quantity = df_ing_quant["Quantity"][i]       
        quantity = parse_fractions(quantity)

        if 'butter' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 227)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.2)
            else:
                conv_value = ""
            output[ingredient] = conv_value
                
        elif 'sugar' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 201)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.2)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 12.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'flour' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 120)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 8)
            else:
                conv_value = ""
            output[ingredient] = conv_value
                
        elif 'baking soda' in ingredient:
            conv_value = convert_ingredient(quantity, 'teaspoon', 6)
            
        elif 'baking powder' in ingredient:
            conv_value = convert_ingredient(quantity, 'teaspoon', 4)
            
        elif 'salt' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 17.06)
            else:
                conv_value = ""
            output[ingredient] = conv_value
        
        elif 'vanilla' in ingredient:
            conv_value = convert_ingredient(quantity, 'teaspoon', 4.2)
            
        elif 'milk' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 245)
            
        elif 'yogurt' in ingredient:
            conv_value = convert_ingredient(quantity, 'cup', 227)
            
        elif 'oil' or 'cooking oil' or 'refined oil' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 198)
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.15)
            else:
                conv_value = ""
            output[ingredient] = conv_value
            
        elif 'water' in ingredient:
            conv_value = convert_ingredient(quantity, 'cup', 237)
            
        elif 'yeast' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 3.11)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value
                
        elif 'chicken' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 125)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chicken mince' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 244)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chicken breast' in ingredient:
            if 'pound' in quantity:
                conv_value = convert_ingredient(quantity, 'pound', 453)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value
                
        elif 'sweet corn' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 145)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value
        
        elif 'spring onion' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 6.51)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value
            
        elif 'carrot' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 116)
            #elif '1/4 cup' in quantity:
            #    conv_value = convert_ingredient(quantity, '1/4 cup', 40)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'corn flour' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 3.16)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 9.38)
            else:
                conv_value = ""
            output[ingredient] = conv_value
            
        elif 'garlic salt' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5.69)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value
            
        elif 'black pepper' or 'pepper' or 'pepper powder'or 'white pepper powder' or 'paprika powder' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.30)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value
            
        elif 'garam masala powder' or 'garam masala' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 1.52)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 4.56)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'vinegar' or 'white vinegar' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.79)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'corn' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 179)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 28.3)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'garlic' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 136)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 8.5)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.81)
            else:
                conv_value = ""
            output[ingredient] = conv_value
        
        elif 'chilli flakes' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 115.2)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7.2)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.44)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'ginger' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 200)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7)
            elif 'inch' in quantity:
                conv_value = convert_ingredient(quantity, 'inch', 12.5)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.17)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'cream cheese' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.1)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'all purpose flour' or 'maida' or 'flour' or 'refined flour' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7.8125)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'peas' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 15.94)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chicken stock' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 240)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 8.47)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'corn starch' or 'cornstarch' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7.5)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 8.47)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'parsley' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 25)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 0.9)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'soy sauce' or 'soya sauce' or 'dark soy sauce' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 16)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 0.9)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'sesame oil' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.67)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 13.6)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'wonton wrapper' in ingredient:
            if 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 28)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 8.47)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'pork' in ingredient:
            if 'pound' or 'lb' in quantity:
                conv_value = convert_ingredient(quantity, 'pound', 453.59)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 28.35)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'rice vine vinegar' or 'vinegar' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.4)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 8.47)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'brown sugar' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 13.8)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 3.54)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'hot sauce' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 19.5)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 6.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chicken broth' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 15.31)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5.1)
            elif 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 258)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'bread crumbs' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 100)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 6.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'green onion' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 52)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 6.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'peanut sauce' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 304)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 6.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'watercress' in ingredient:
            if 'pound' in quantity:
                conv_value = convert_ingredient(quantity, 'pound', 453)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'ginger garlic paste' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 16)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value
                
        elif 'peanut oil' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'red chili powder' or 'chilli powder' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 5.38)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'cabbage' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 200)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'bean sprouts' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 213)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 28.35)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'spring roll' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 244)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chilli garlic sauce' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 288)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 18)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 6)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'cilantro' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 17)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'vegetable oil' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 220)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'tomato ketchup' or 'tomato sauce' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.1)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chilli sauce' or 'red chilli sauce' or 'green chili sauce' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 264)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 16.5)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'capsicum' or 'red capsicum' or 'yellow capsicum' or 'green capsicum' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 85)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'bell pepper' or 'red bell pepper' or 'yellow bell pepper' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 150)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 7)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'cauliflower' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 108)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 6.75)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.25)
            else:
                conv_value = ""
            output[ingredient] = conv_value
                
        elif 'green beans' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 83)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 5.19)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 1.73)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'coriander leaves' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 16)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 1)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 0.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'paneer' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 210)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 13.13)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.38)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'scallions' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 100)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 6.25)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.08)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'ajinomoto' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 248)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 15.5)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5.17)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'lemon juice' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 230)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.4)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.79)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'vegetable stock' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 191)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 11.9)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 0.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'salt' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 115.2)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7.2)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.4)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'turmerice powder' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 96)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 6)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'food color' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 288)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 18)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 6)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'coriander leaves' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 16)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 1)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 0.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'noodles' or 'egg noodles' or 'rice noodles' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 37.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'coconut milk' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 240)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 15)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5)
            elif 'oz' in quantity:
                conv_value = convert_ingredient(quantity, 'oz', 28.5)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'cumin seed' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.03)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'chilli oil' in ingredient:
            if 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 14)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'tofu' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 217)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 13.56)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.52)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'peanuts' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 112)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 7)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 2.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'broccoli' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 220)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 13.75)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.58)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'curry powder' in ingredient:
            if 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 6.39)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 0.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'curd' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 226)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 14.13)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 4.71)
            else:
                conv_value = ""
            output[ingredient] = conv_value

        elif 'mushroom' in ingredient:
            if 'cup' in quantity:
                conv_value = convert_ingredient(quantity, 'cup', 256)
            elif 'tablespoon' in quantity:
                conv_value = convert_ingredient(quantity, 'tablespoon', 16)
            elif 'teaspoon' in quantity:
                conv_value = convert_ingredient(quantity, 'teaspoon', 5.33)
            else:
                conv_value = ""
            output[ingredient] = conv_value        
            
        else:
            conv_value = ""
            output[ingredient] = conv_value
            
    print(output)
    
    return output
