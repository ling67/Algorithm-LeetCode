// Sliding Window

class Solution {
    public String minWindow(String s, String t) {

        if (s.length() == 0 || t.length() == 0) {
            return "";
        }

        Map<Character, Integer> tmap = new HashMap<>();
        for (char ch : t.toCharArray()) {
            tmap.put(ch, tmap.getOrDefault(ch, 0) + 1);
        }

        int l = 0;
        String res = s + s;
        Map<Character, Integer> smap = new HashMap<>();
        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);
            smap.put(ch, smap.getOrDefault(ch, 0) + 1);

            while (l <= r && satisfy(smap, tmap)) {
                if ( r - l + 1 < res.length()) {
                    res = s.substring(l, r + 1);
                }

                char lch = s.charAt(l);
                smap.put(lch, smap.get(lch) - 1);
                l++;
            }
        }
        
        return res.equals(s + s) ? "" : res;
    }

    private boolean satisfy(Map<Character, Integer> s, Map<Character, Integer> t) {
        for (Map.Entry<Character, Integer> entry: t.entrySet()) {
            char key = entry.getKey();
            if (s.getOrDefault(key, 0) < entry.getValue()) {
                return false;
            }
        }
        return true;
    }
}
