require 'text'
require 'text/hyphen'

animals = open("animals.txt").read.split("\n").select{ | w | w.split(" ").length == 1}


@ans = animals.collect{ | a | [a, Text::Metaphone.double_metaphone(a)[0]]}
@en = Text:: Hyphen.new(: left = > 0, : right = > 0)
def animalize_word word
   parts = @en.visualize(word).split(/-/)
    parts_with_phone = parts.collect{| p | [p, Text::Metaphone.double_metaphone(p)[0]]}

    rhymed_parts = parts_with_phone.collect do | part|
        @ans.select{ | a | a[1] == part[1]}
    end

    replaceable_parts = []
    rhymed_parts.each_with_index do | part, i|
       if !part.empty?
           puts part.inspect
            puts
            replaceable_parts << [i, part.sample[0]]
        end
    end

    results = []
    replaceable_parts.each do | index, part|
       name = []
        parts.each_with_index do | word, i|
           if i == index
               name << part
            else
               name << word
            end
        end
        results << name.join("")
    end

    return results

end


def generate_animal_name name
    parts = name.split( /\s/)
    part_options = {}
    parts.each do | part|
       part_options[part] = animalize_word(part)
    end

    output = []

    part_options.each do | word, animalizations|
        animalizations.each do | animal|
           result = []
            parts.each do | part|
               if part == word
                   result << animal
                else
                   result << part
                end
            end
            output << result.join(" ")
        end
    end

    output

end

puts generate_animal_name(ARGV[0])
