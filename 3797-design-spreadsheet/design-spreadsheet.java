class Spreadsheet {
    private Map<String,Integer>spreadsheet= new HashMap<>();



    public Spreadsheet(int rows) {
       
    }
    
    public void setCell(String cell, int value) {
        spreadsheet.put(cell,value);
    }
    
    public void resetCell(String cell) {
        spreadsheet.put(cell,0);
    }
    
    public int getValue(String formula) {
        String input=formula.substring(1);
        String[] operands=input.split("\\+");
        int num1=0;
        int num2=0;
        if(isInteger(operands[0])){
            num1=Integer.parseInt(operands[0]);
        }
        else{
            num1= spreadsheet.getOrDefault(operands[0],0);
        }
        if(isInteger(operands[1])){
            num2=Integer.parseInt(operands[1]);
        }
        else{
            num2=spreadsheet.getOrDefault(operands[1],0);
        }
        return num2+num1;


        
    }
    private boolean isInteger(String str){
        try{
            Integer.parseInt(str);
            return true;
        }
        catch(NumberFormatException e){
            return false;
        }
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */