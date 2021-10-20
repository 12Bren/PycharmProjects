/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package helloworld;

/**
 *
 * @author b
 */
public class HelloWorld {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        /* = */ byte first = 5;
        /* += */ first += 5; //read as 5+5
        /* -+ */ first -= 5; //read as 5-5
        /* *= */ first *= 5; //read as 5*5
        /* /= */ first /= 5; //read as 5/5
        /* %= */ first %= 5; //read as 5%5
        /* &= */ first &= 5; //read as 5&5
        /* |= */ first |= 5; //read as 5!5
        /* ^= */ first ^= 5; //read as 5^5
        /* >>= */first = 120;
        /* <<= */
        System.out.println(first);
        //--------------------------------
        
        //Comparison operators are used to compare two values:
        
        // ==  Equal to 
        // !=  Not equal
        // >  Greater than
        // <   Less than
        // >=  Greater than or equal to
        // <=  Less than or equal to
        //--------------------------------
        
        //Logical operators are used to determine the logic between variables or values:
        
        // &&  	Logical and 	Returns true if both statements are true 	x < 5 &&  x < 10
        // ||  	Logical or 	Returns true if one of the statements is true 	x < 5 || x < 4
        // ! 	Logical not 	Reverse the result, returns false if the result is true   !(x < 5 && x < 10)
        //----------------------------------
        
        //Arithmetic operators are used to perform common mathematical operations.
        
        /* + */ float second = (byte) first + 4f;
        /* - */ second = 5 - first;
        /* * */ second = 5 * first;
        /* / */ second = 5 / first;
        /* % */ second = 5 % first;
        /* ++ */second = first ++;
        /* -- */second = first --;
        
        System.out.println(second);
        
        
        
        
    }
    
}
