import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class Day_1_2 {

    public static void main(String[] args) {
        try(Stream<String> mass = Files.lines(Paths.get("Day_1/day_1.txt"))) {
            int totalFuel = mass
                    .map(Integer::valueOf)
                    .mapToInt(Day_1_2::countTotalMass)
                    .sum();

            System.out.println(totalFuel);
        } catch(IOException e) {

        }
    }

    private static int countTotalMass(Integer i) {
        int totalMass = 0;
        int currentMassToCount = i / 3 - 2;

        do {
            totalMass += currentMassToCount;
            currentMassToCount = currentMassToCount / 3 - 2;
        } while (currentMassToCount > 0);

        return totalMass;
    }

}
