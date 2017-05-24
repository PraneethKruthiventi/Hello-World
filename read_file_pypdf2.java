import java.io.*;
//import com.csvreader.CsvWriter;

public class read_file_pypdf2 {
    public static void main(String [] args) 
    {

        // The name of the file to open.
        String fileName = "data.txt";

        //output file
        String outputFile = "data.csv";

        // This will reference one line at a time
        String line = null;

        //stores the column titles in an array
        String[] columnName = { "Name of the contact",
                                "Dt Number",};

        //stores the keyword
        String[] keyword = {"ContactEmail[0]",
                             "EmpNum[0]",    };        

        String data = "";

        //constants
        int flag = 0;
        int i = 0;
        int j = 0;
        int search = 0;
        int position = -1;

        try
        {
            // FileReader reads text files in the default encoding.
            FileReader fileReader = new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            /*
            //open csv file
            CsvWriter csvOutput = new CsvWriter(new FileWriter(outputFile, true), ',');

            //assign header in the csv file
            csvOutput.write("Request type");
            csvOutput.write("Information");
            csvOutput.endRecord();*/

            while((line = bufferedReader.readLine()) != null)
            {
                int str_length = line.length();
                for(i = 0, j = 0; i < str_length; i++) 
                {
                    if(search == 1)
                    {
                        if(line.charAt(i) == ')')
                        {
                            search = 0;
                            data = data.substring(0,data.length()-1);
                            System.out.println( columnName[j] + " ------- " + data);
                            j++;
                            data = "";
                        }
                        else
                        {
                            data += line.charAt(i);
                        }
                    }
                    while(search != 1)
                    { 
                        for( ; j < 2; j++)
                        {
                            position = line.indexOf(keyword[j]); 
                            if(position == -1)
                                break;
                            position += keyword[j].length() + 3;
                            i = position - 1;
                            System.out.println("i " + i);
                            search = 1;
                            break;
                        }
                        if(position == -1)
                            break;
                    }   
                    if(position == -1)
                        break;



                    /*if(br == 1)
                    {
                        br = 0;
                        break;
                    }
                    if(line.equals(dataArray[i]) && flag == 0)
                    {
                        flag = 1;
                        br = 1;
                        data =  dataArray[i];
                        //System.out.println("Hello there");
                        continue;
                    }
                    if(flag == 1)
                    {
                        System.out.println(data + "------ " + line);
                        /*csvOutput.write("Request type");
                        csvOutput.write("Information");
                        csvOutput.endRecord();/
                        flag = 0;
                        break;
                    }*/
                }

            }
            
            /*while((line = bufferedReader.readLine()) != null)
            {
                System.out.println(line + " " + i + " " + line.equals("I returned from the City about three o'clock on that"));
                i++;
            }*/ 

            // Always close files.
            bufferedReader.close();         
        }
        catch(FileNotFoundException ex) 
        {
            System.out.println(
                "Unable to open file '" + 
                fileName + "'");                
        }
        catch(IOException ex) 
        {
            System.out.println
            ("Error reading file " + fileName + "'");                  
            // Or we could just do this: 
            // ex.printStackTrace();
        }
    }

}
