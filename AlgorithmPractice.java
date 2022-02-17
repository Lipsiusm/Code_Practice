public class AlgorithmPractice{
	public static void main(String [] args){

	int [] random_array = {12,4,11,9,6,7,5,1,3,2,8,10};

	//printing out the unsorted list
	System.out.println("Unsorted Array: ");
	for (int a=0; a<random_array.length; a++){
		System.out.print(random_array[a] + " ");
	}
	//initializing into some number in the array
	int temp = random_array[0];

	for (int i=0; i < random_array.length-1; i++){
		for (int k= i + 1; k < random_array.length; k++){
			if (random_array[k] < random_array[i]){
				temp = random_array[i];
				random_array[i] = random_array[k];
				random_array[k] = temp;
			}
		}
	}
	//printing out the sorted list
	System.out.println("Sorted List:");
	for (int b=0; b<random_array.length; b++){
		System.out.print(random_array[b] + " ");
	}
	}
} 