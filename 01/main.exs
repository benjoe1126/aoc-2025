defmodule AocUtil do
  defp sign(x) do
    case String.first(x) do
      "L" -> - 1
      "R" -> 1
    end
  end
  defp rot_to_num(x) do
    a = String.slice(x,1..-1) |> String.to_integer()
    a * sign(x)
  end

  def get_pos(rot, pos) when rot + pos >= 0 do
    rem(rot + pos,100)
  end
  def get_pos(rot, pos) when rot + pos < 0 do
    rem(100 + rem(rot,100) + pos,100)
  end

  def readFile(fname) do
    File.stream!(fname) |> Enum.map(fn x -> String.trim_trailing(x) |> rot_to_num() end)
  end
end

defmodule Solution do
  defmodule PartOne do
    def solve([ rot | tail ], 0, accum)  do
      solve(tail, AocUtil.get_pos(rot,0), accum + 1)
    end

    def solve([ rot | tail ], pos, accum) do
      solve(tail, AocUtil.get_pos(rot,pos), accum)
    end

    def solve([], _ , accum) do
      accum
    end
  end
  defmodule PartTwo do
    defp times_zero_hit(rot, pos)  do
      n_rot = rem(rot, 100)
      n_pos = AocUtil.get_pos(n_rot,pos)
      accum =  abs(trunc(rot / 100))
      if ((n_rot + pos) > 99) or (pos != 0 and (n_rot + pos) < 0) or (n_rot != 0 and n_pos == 0) do
        accum + 1
      else
        accum
      end

    end
    def solve([],_, accum) do
      accum
    end
    def solve( [rot | tail], pos, accum) do
        solve(tail, AocUtil.get_pos(rot,pos),accum + times_zero_hit(rot,pos))
    end
    end
  end

AocUtil.readFile("input.txt") |> Solution.PartOne.solve(50,0) |> IO.inspect()
AocUtil.readFile("input.txt") |> Solution.PartTwo.solve(50,0) |> IO.inspect()
