import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class Day_1_1 {

    public static void main(String[] args) throws IOException {
        Stream<String> mass = Files.lines(Paths.get("Day_1/day_1.txt"));
        int sum = mass
                    .map(Integer::valueOf)
                    .map(input -> input / 3)
                    .mapToInt(input -> input - 2)
                    .sum();
        System.out.println(sum);
    }

}
